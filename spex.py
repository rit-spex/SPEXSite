from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/second/')
def second():
    text= "Projects"
    return render_template('second.html', text=text)
