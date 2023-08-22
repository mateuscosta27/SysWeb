from flask import Blueprint


backup_bp = Blueprint("backup_bp", __name__)


@backup_bp.route("/backup", methods=["GET"])
def get_all_clients():
    return 'Rota de backups'