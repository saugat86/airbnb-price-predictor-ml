from flask import Blueprint, jsonify, request, abort
from services import stats_service
from flask_httpauth import HTTPBasicAuth
from airbnb_base_logger import logger


api = Blueprint(
    name="stats_controller",
    import_name="stats_controller",
    url_prefix="/stats"
)


@api.route("/")
# @auth.login_required
def get_stats():
    """
    Get request to get statistics for the airbnbs
    """
    log_msg = f"Attempting to retrieve airbnb data from {request.remote_addr}"
    data = stats_service.main()
    return (data), 200
