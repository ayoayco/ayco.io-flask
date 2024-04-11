from flask import Flask, send_from_directory
from partials import partials
import datetime

app = Flask(__name__)
app.register_blueprint(partials, url_prefix='/p')

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
