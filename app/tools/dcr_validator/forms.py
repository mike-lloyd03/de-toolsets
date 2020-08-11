from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField

class UploadForm(FlaskForm):
    dcr_list = FileField('dcr_list')
    wo_list = FileField('wo_list')
    submit = SubmitField('Submit')
