from app import create_app


app_test = create_app()

def test_stats():
    """
    GIVEN: that the app running 
    WHEN  stats  route is called
    THEN check is response is a redirection to stats service 
    """
    with app_test.test_client() as test_client:

        response = test_client.get("/stats")

        assert response.status_code == 308
        