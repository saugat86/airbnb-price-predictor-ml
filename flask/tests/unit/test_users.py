from controllers.airbnb_controller import users


def test_new_user():
    """
    GIVEN: users 
    WHEN  
    THEN check username in list 
    """
    assert 'link' in list(users.keys())
    assert 'jenny' in list(users.keys())
