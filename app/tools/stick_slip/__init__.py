from flask import Blueprint

bp = Blueprint('stick_slip', __name__,
               template_folder='templates',
               static_folder='static'
               # static_folder='app/tools/stick-slip/static',
               # static_url_path=f'{bp.static_url_path}/static'
               )

# from app.tools.stick_slip import routes
from . import routes
