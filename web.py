from flask import Flask, send_from_directory
import sentry_sdk
import json

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

# /threads
try:
    from threads.threads import threads
    app.register_blueprint(threads, url_prefix='/threads')
    print(' * Threads blueprint registered')
    from threads.cache import cache as thread_cache
    print(' * Threads cache type: ' + app.config["CACHE_TYPE"])
    thread_cache.init_app(app)
except ImportError:
    print(' ! Threads blueprint not found')

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
    return send_from_directory('dist', 'index.html')

@app.route('/<path:path>')
def dist(path):
    if '.' in path:
        return send_from_directory('dist', path)
    else:
        return send_from_directory('dist', path + '/index.html')

@app.errorhandler(404)
def not_found(e):
    return send_from_directory('dist', '404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')

