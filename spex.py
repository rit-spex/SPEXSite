from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hab/')
def hab():
    return render_template('hab.html')


@app.route('/cubesat/')
def cubesat():
    return render_template('cubesat.html')


@app.route('/spexcast/')
def spexcast():
    return render_template('spexcast.html')

@app.route('/getInvolved/')
def getInvolved():
    return render_template('getInvolved.html')
	
@app.route('/CGPAD')
def cgpad():
	return render_template('cgpad.html')

@app.route('/sponsors/')
def sponsors():
    return render_template('sponsors.html')

@app.route('/donate/')
def donate():
    return render_template('donate.html')

@app.route('/statistics/')
def stats():
    return redirect('http://habtelemetry.app.csh.rit.edu/#/statistics')

@app.route('/orientation/')
def orientation():
    return redirect('http://habtelemetry.app.csh.rit.edu/#/orientation')

@app.route('/astrodynamics/')
def astro():
    return render_template('astro.html')

@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml')
