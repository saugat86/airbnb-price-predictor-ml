from app import create_app


app_test = create_app()

def test_airbnb():
    """
    GIVEN 
    WHEN 
    THEN  
    """
    with app_test.test_client() as test_client:


        # Unauthorized access
        response = test_client.get("/airbnb/2")
        assert response.status_code == 401

    