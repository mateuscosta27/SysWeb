from flask import Blueprint


client_bp = Blueprint("client_bp", __name__)


@client_bp.route("/", methods=["GET"])
def get_all_clients():
    return 'Rota de clientes'