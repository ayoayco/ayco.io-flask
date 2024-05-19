from flask import Flask, send_from_directory
import sentry_sdk
import json
from cache.cache import cache

app = Flask(__name__)

try:
    from threads.threads import threads
    app.register_blueprint(threads, url_prefix='/threads')
    print(' * Threads blueprint registered')
except ImportError:
    print(' ! Threads blueprint not found')

app.config.from_file("config.json", load=json.load)

# caching
print(' * Cache type: ' + app.config["CACHE_TYPE"])
cache.init_app(app)

# perf monitoring & error tracking
sentry_config = app.config["SENTRY"]
print(' * Monitoring DSN: ' + sentry_config["dsn"])
sentry_sdk.init(
    dsn=sentry_config["dsn"],
    traces_sample_rate=sentry_config["traces_sample_rate"],
    profiles_sample_rate=sentry_config["profiles_sample_rate"],
    enable_tracing=sentry_config["enable_tracing"],
)

@app.route('/')
def home():
    try:
        return send_from_directory('dist', 'index.html')
    except:
        print(' ! dist folder missing')
        return 'dist folder missing'

@app.route('/<path:path>')
def dist(path):
    try:
        if '.' in path:
            return send_from_directory('dist', path)
        else:
            return send_from_directory('dist', path + '/index.html')
    except:
        print(' ! dist folder missing')
        return 'dist folder missing'

@app.errorhandler(404)
def not_found(e):
    return send_from_directory('dist', '404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')

