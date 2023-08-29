from flask import Blueprint

api = Blueprint(
    name="ping_controller",
    import_name="ping_controller",
    url_prefix="/ping"
)


@api.route("/")
def ping():
    """
    Just a ping endpoint
    """
    return "Pong"
