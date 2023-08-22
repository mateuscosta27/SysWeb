from flask import Blueprint


site_bp = Blueprint("site_bp", __name__)


@site_bp.route("/site", methods=["GET"])
def get_all_clients():
    return 'Rota de site'