from flask import Flask, send_from_directory
from flask_caching import Cache
import sentry_sdk
import json
from partials import partials
from threads.threads import threads

app = Flask(__name__)
app.register_blueprint(partials, url_prefix='/p')
app.register_blueprint(threads, url_prefix='/threads')
app.config.from_file("config.json", load=json.load)

# caching
cache = Cache()
cache.init_app(app)
print(' * Cache type: ' + app.config["CACHE_TYPE"])

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

