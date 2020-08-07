import os

from flask import render_template, redirect, url_for, request
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from . import bp
from .forms import UploadForm
from .static.filterTDMS import filter_and_interpolate_data

@bp.route('/')
def stick_slip_upload_form():
    form = UploadForm()
#    static_folder = os.path.join(bp.static_folder, 'temp')
#    for file in os.listdir(static_folder): 
#        os.remove(static_folder + '/' + file)
    return render_template('upload.html', form=form)

@bp.route('/', methods=['GET', 'POST'])
def stick_slip_results_view():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        filename = os.path.join(bp.static_folder, 'temp/' + filename)
        uploaded_file.save(filename)
        output_img = filter_and_interpolate_data(filename)
        print(output_img)
#        os.remove(filename)
    else:
        return redirect(url_for('stick_slip.stick_slip_upload_form'))
    return render_template('results_view.html', output_img=output_img)
