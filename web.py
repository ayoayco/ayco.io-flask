from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/showcase')
def showcase():
    return render_template('showcase.html')

@app.route('/stuff')
def stuff():
    return render_template('stuff.html')

@app.route('/now')
def now():
    return render_template('now.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
