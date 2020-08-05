import os

from flask import render_template, redirect, url_for, request
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from app.tools.stick_slip import bp
from .static.filterTDMS import filter_and_interpolate_data

@bp.route('/')
def stick_slip_upload_form():
    print(bp.static_url_path)
    return render_template('upload.html')

@bp.route('/', methods=['GET', 'POST'])
def stick_slip():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    # filename = os.path.join('app/tools/stick_slip/static', filename)
    if filename != '':
        # filename = url_for('stick_slip.static', filename=filename)
        filename = os.path.join(bp.static_folder, filename)
        uploaded_file.save(filename)
        output_img = filter_and_interpolate_data(filename)
        print(output_img)
        os.remove(filename)
    else:
        return redirect(url_for('stick_slip.stick_slip_upload_form'))
    return render_template('results_view.html', output_img=output_img)
    # return filename

@bp.route('/cwd')
def cwd():
    return os.getcwd()
