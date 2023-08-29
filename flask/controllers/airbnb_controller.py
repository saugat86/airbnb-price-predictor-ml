from flask import Blueprint, jsonify, request, abort
from services import airbnb_service
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from airbnb_base_logger import logger

api = Blueprint(
    name="airbnb_controller",
    import_name="airbnb_controller",
    url_prefix="/airbnb"
)

users = {
    "link": generate_password_hash("42"),
    'jenny': generate_password_hash("1997")
}

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@api.route("/")
@auth.login_required
def get_all_airbnb():
    """
    Get request to get all airbnb. It accepts queries for neighbourhood,
    price min and max, room type and accommodates
    """
    neighbourhood = request.args.get(
        'neighbourhood') if request.args.get('neighbourhood') else "all"
    price_min = request.args.get(
        'price_min') if request.args.get('price_min') else "all"
    price_max = request.args.get(
        'price_max') if request.args.get('price_max') else "all"
    room_type = request.args.get(
        'room_type') if request.args.get('room_type') else "all"
    accommodates = request.args.get(
        'accommodates') if request.args.get('accommodates') else "all"

    log_msg = f"Attempting to retrieve airbnb data from {request.remote_addr}"
    logger.info(f"{log_msg}, query params: neighbourhood {neighbourhood}, price_min {price_min}, price_max {price_max}, \
                room_type {room_type}, accommodates {accommodates} ")
    airbnb = airbnb_service.get_all_airbnb(
        neighbourhood, price_min, price_max, room_type, accommodates)

    return jsonify(airbnb), 200


@api.route("/<int:id>")
@auth.login_required
def get_airbnb_by_id(id):
    """
    Get airbnb based on id
    """
    logger.info(f"Attempting to get airbnb {id} from {request.remote_addr}")
    airbnb = airbnb_service.get_airbnb_by_id(id)
    if not airbnb:
        logger.error(f"Could not retrieve airbnb {id}")
        abort(400)
    return jsonify(airbnb), 200


@api.route("/", methods=['POST'])
@auth.login_required
def save_airbnb():
    """
    Post request to save new airbnb in repo
    """
    logger.info(
        f"Attempting to save airbnb {request.get_json()} from {request.remote_addr}")
    airbnb = request.get_json()
    result = airbnb_service.save(airbnb)
    if not result:
        logger.error(
            f"Could not save airbnb {request.get_json()} from {request.remote_addr}")
        abort(400)
    logger.info(f"Airbnb {airbnb} saved")

    return jsonify(result), 200


@api.route("/<int:id>", methods=['DELETE'])
@auth.login_required
def delete_airbnb_by_id(id):
    """
    Delete request to delete an airbnb based on id from repo
    """
    result = airbnb_service.delete_airbnb(id)
    if not result:
        logger.error(f"Could not delete airbnb {id}")
        abort(500)
    if result.get("error"):
        logger.error(f"Could not delete airbnb {id}")
        abort(404)
    return jsonify(result)
