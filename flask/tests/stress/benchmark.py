from locust import HttpUser, between, task
import random


class WebsiteUser(HttpUser):

    wait_time = between(1, 1.5)

    def on_start(self):
        self.uid = str(random.randint(0, 100_000)).zfill(6)

    @task
    def attempt_ping(self):

        self.client.get("/ping")

    @task
    def get_stats(self):

        self.client.get("/stats")

    @task
    def get_airbnb_100(self):

        self.client.get("/airbnb/100", auth=('link', 42))

    @task
    def get_airbnb_20(self):

        self.client.get("/airbnb/20", auth=('link', 42))

    @task
    def get_all_airbnb(self):

        self.client.get("/airbnb", auth=('link', 42))

    @task
    def post_airbnb(self):

        self.client.post("/airbnb", auth=('link', 42), json={
            "Dist_Acropolis": "0.309351946",
            "Dist_Syntagma": "0.612897077",
            "accommodates": "3",
            "availability_30": "0",
            "availability_365": "314",
            "availability_60": "28",
            "availability_90": "53",
            "bathrooms": "1",
            "beds": "1",
            "has_availability": "1",
            "has_license": "1",
            "host_has_profile_pic": "1",
            "host_identity_verified": "1",
            "host_is_superhost": "1",
            "id": "242",
            "instant_bookable": "1",
            "maximum_minimum_nights": "2",
            "maximum_nights": "1125",
            "maximum_nights_avg_ntm": "1125",
            "minimum_maximum_nights": "1125",
            "minimum_nights": "2",
            "minimum_nights_avg_ntm": "2",
            "neighbourhood": "EMPORIKO TRIGONO-PLAKA",
            "number_of_reviews": "335",
            "price": "59",
            "reviews_per_month": "3.86",
            "room_type": "Entire home/apt"
        }

        )

    @task
    def post_models(self):

        self.client.post("/models", json={"host_is_superhost": "t",
                                          "host_has_profile_pic":    "f",
                                          "host_identity_verified": "t",
                                          "neighbourhood_cleansed": "ΚΟΥΚΑΚΙ",
                                          "property_type":   "Entire rental unit",
                                          "room_type":   "Entire home/apt",
                                          "accommodates": 3,
                                          "bathrooms_text": "'Half-bath",
                                          "beds":    3,
                                          "minimum_nights":  4,
                                          "maximum_nights":  4,
                                          "maximum_minimum_nights": 4,
                                          "minimum_maximum_nights":  4,
                                          "maximum_nights_avg_ntm": 4,
                                          "minimum_nights_avg_ntm":  4,
                                          "has_availability":    "t",
                                          "availability_30": 45,
                                          "availability_60": 294,
                                          "availability_90": 90,
                                          "availability_365": 201,
                                          "number_of_reviews": 4,
                                          "instant_bookable":    "f",
                                          "reviews_per_month": 0.04,
                                          "license": "13589523",
                                          "latitude": 37.986130,
                                          "longitude": 23.739230}

                         )
