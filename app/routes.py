from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from app import app
from app.static.test import testfunc
from app.static.stick_slip_tools.filterTDMS import filter_and_interpolate_data

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/upload')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if uploaded_file.filename != '':
        uploaded_file.save(filename)
        filter_and_interpolate_data(filename)
        del(filename)
    return redirect(url_for('index'))
