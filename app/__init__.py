from flask import Flask


from .controller.cliente_controller import client_bp
from .controller.site_controller import site_bp
from .controller.backup_controller import backup_bp


app = Flask(__name__)


app.register_blueprint(client_bp)
app.register_blueprint(site_bp)
app.register_blueprint(backup_bp)