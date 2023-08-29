from xmlrpc.client import ResponseError
from services import stats_service, models_service, airbnb_service 


def test_services():
    
    response = stats_service.main()
    assert type(response) is dict
