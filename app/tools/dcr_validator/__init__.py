from flask import Blueprint

bp = Blueprint('dcr_validator', __name__,
               template_folder='templates',
               static_folder='static'
               )

from . import routes
