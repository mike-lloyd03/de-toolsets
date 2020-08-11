from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secrets'

from app import routes
bootstrap = Bootstrap(app)

from app.tools.stick_slip import bp as stick_slip_bp
app.register_blueprint(stick_slip_bp, url_prefix='/tools/stick-slip')

from app.tools.dcr_validator import bp as dcr_validator_bp
app.register_blueprint(dcr_validator_bp, url_prefix='/tools/dcr-validator')
