from app import create_app


app_test = create_app()

def test_ping():
    """
    GIVEN: that the app running 
    WHEN  ping route is called
    THEN check is response is 'Pong',200 
    """
    with app_test.test_client() as test_client:

        response = test_client.get("/ping/")
        assert response.status_code == 200
        assert response.data == b'Pong'
