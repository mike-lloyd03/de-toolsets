import os

from flask import render_template, redirect, url_for, request
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from app.tools.stick_slip import bp
from .static.filterTDMS import filter_and_interpolate_data

@bp.route('/stick-slip')
def stick_slip_upload_form():
    return render_template('upload.html')

@bp.route('/stick-slip', methods=['GET', 'POST'])
def stick_slip():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    filename = os.path.join('app/tools/stick_slip/data_files', filename)
    print(filename)
    if filename != '':
        uploaded_file.save(filename)
        output_img = filter_and_interpolate_data(filename)
        # del(filename)
    return render_template('results_view.html', output_img=output_img)
