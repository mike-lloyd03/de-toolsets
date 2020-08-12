import os

from flask import render_template, redirect, url_for, request
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from . import bp
from .forms import UploadForm
from .static.DCR_Validator import dcr_validator

@bp.route('/')
def dcr_validator_upload_form():
    form = UploadForm()
    # static_folder = os.path.join(bp.static_folder, 'temp')
    # for file in os.listdir(static_folder): 
    #     os.remove(static_folder + '/' + file)
    return render_template('dcr_upload.html', form=form)

@bp.route('/', methods=['GET', 'POST'])
def dcr_validator_results_view():
    wo_file = request.files['wo_file']
    dcr_file = request.files['dcr_file']
    wo_filename = secure_filename(wo_file.filename)
    dcr_filename = secure_filename(dcr_file.filename)
    if wo_filename != '' and dcr_filename != '':
        static_temp_dir = os.path.join(bp.static_folder, 'temp')
        if not os.path.isdir(static_temp_dir):
            os.mkdir(static_temp_dir)
        wo_filename = os.path.join(bp.static_folder, 'temp/' + wo_filename)
        dcr_filename = os.path.join(bp.static_folder, 'temp/' + dcr_filename)
        wo_file.save(wo_filename)
        dcr_file.save(dcr_filename)
        output_file = dcr_validator(wo_filename, dcr_filename)
        # os.remove(filename)
    else:
        return redirect(url_for('dcr_validator.dcr_validator_upload_form'))
    return render_template('dcr_results_view.html', output_file=output_file)
