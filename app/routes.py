from os import path
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tools')
def tools():
    tool_list = [
        {'name': 'stick-slip', 'display_name': 'Stick Slip Testing'},
        {'name': 'dcr-validator', 'display_name': 'DCR Validator'}
    ]
    return render_template('tools.html', tool_list=tool_list)

