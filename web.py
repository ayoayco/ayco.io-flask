from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('dist', 'index.html')

@app.route('/<path:path>')
def dist(path):
    if '.' in path:
        return send_from_directory('dist', path)
    else:
        return send_from_directory('dist', path + '/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
