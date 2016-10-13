from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/hab/')
def hab():
    return render_template('hab.html')


@app.route('/cubesat/')
def cubesat():
    return render_template('cubesat.html')


@app.route('/spexcast/')
def spexcast():
    return render_template('spexcast.html')
