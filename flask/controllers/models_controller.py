import json
from tempfile import tempdir
from flask import Blueprint, jsonify, request
from services import models_service
from flask_httpauth import HTTPBasicAuth
from airbnb_base_logger import logger
import warnings
warnings.filterwarnings("ignore")

api = Blueprint(
    name="models_controller",
    import_name="models_controller",
    url_prefix="/models"
)


@api.route("", methods=['POST'])
def get_prediction():
    """
    Get request to predict the price of an Airbnb. The license column needs 
    to be either empty or has a value.
    """
    log_msg = f"Attempting to retrieve airbnb data from {request.remote_addr}"
    data = request.get_json()
    temp_dict = data.copy()
    del temp_dict['license']
    if "" in temp_dict.values():
        keys = [k for k, v in temp_dict.items() if v == ""]
        s = "Fill cells: "
        for k in keys:
            s += k
            s += ", "
        return s, 200

    prediction = models_service.main(data)
    return prediction, 200
