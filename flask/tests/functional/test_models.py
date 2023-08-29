from app import create_app


app_test = create_app()



def test_stats():
    """
    GIVEN: that the app running 
    WHEN  models  route is called
    THEN check if response is  
    """
    post_data = {"host_is_superhost" : "t",
"host_has_profile_pic" :    "f",
"host_identity_verified" :"t"   ,
"neighbourhood_cleansed" : "ΚΟΥΚΑΚΙ",
"property_type" :   "Entire rental unit",
"room_type" :   "Entire home/apt",
"accommodates" : 3,
"bathrooms_text" : "'Half-bath",
"beds" :    3,
"minimum_nights" :  4,
"maximum_nights" :  4,
"maximum_minimum_nights" : 4    ,
"minimum_maximum_nights" :  4,
"maximum_nights_avg_ntm" : 4,
"minimum_nights_avg_ntm" :  4,
"has_availability" :    "t",
"availability_30" : 45,
"availability_60" : 294,
"availability_90" : 90,
"availability_365" : 201,
"number_of_reviews" : 4 ,
"instant_bookable" :    "f",
"reviews_per_month" :0.04,
"license" : "13589523",
"latitude" :37.986130,
"longitude" :   23.739230}
    
    with app_test.test_client() as test_client:

        # 405 Method Not Allowed. The method is post
        response = test_client.get("/models")
        assert response.status_code == 405
  