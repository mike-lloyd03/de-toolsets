from flask import render_template, request, redirect, url_for

from app import app
from app.static.test import testfunc

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/upload')
def upload_form():
    

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))
