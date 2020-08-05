from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

from app import routes
bootstrap = Bootstrap(app)

from app.tools.stick_slip import bp as stick_slip_bp
app.register_blueprint(stick_slip_bp, url_prefix='/tools/stick-slip')
