from flask import Blueprint

bp = Blueprint('stick_slip', __name__,
               template_folder='templates',
               static_folder='static'
               )

from . import routes
