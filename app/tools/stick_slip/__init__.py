from flask import Blueprint

bp = Blueprint('stick_slip', __name__, template_folder='templates')

from app.tools.stick_slip import routes
