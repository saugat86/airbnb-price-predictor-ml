<h1> <strong> Flask App Project</h1> </strong>


<h2> <strong> Code Structure </h2> </strong>
<br>


#### Top level
- <b>app.py</b>: Applications entrypoint. Used to start the webserver. Here we register our blueprints
- <b>airbnb_base_logger.py</b>: Logger for incoming information

<br>

#### Controllers
One file per logical unit: <br>

- <b>ping</b>: Typical ping endpoint.
- <b>stats</b>: Declares the endpoint where we can request the statistics.
- <b>models</b>: Accepts data for an individual Airbnb listing and returns a predicted price.
- <b>airbnb</b>: Supports basic HTTP requests. GET, POST (to be implemented), DELETE an airbnb based on id. 

<br>

#### Repo
The data storage of the application. Should include the airbnb.csv initially.
In case you delete or update something on the dataset, you can always replace 
it with the original_airbnb_copy.csv and bring it to its original state. Here 
you can find and the trained-model that runs in the background for the price
prediction

<br>

#### Services

The business logic of our app. 

- <b>stats</b>: Functions that calculate several stats based on aggregations by utilized the pandas lib.
- <b>models</b>: Functions that perform all the preprocessing on the input data and use the pre-trained model to predict the price of the listing.
- <b>aibnb</b>: Mappings, utilities and anything else needed to work with the airbnb resource.

<br>

#### Test

Execute basic tests for the app.

```
python -m pytest
```


Execute stress tests 

```
pip install locust uvicorn
python app.py
locust --host http://localhost:5000   -f tests/stress/benchmark.py
```

or run test resuls on the terminal. Ex. 10 users with spanning rate 5.
```
locust --host http://localhost:5000   -f tests/stress/benchmark.py --headless --host http://localhost:5000 -u 10 -r 5
```

From here you get a user interface. It's typically available at 0.0.0.0:8089 
unless you've changed the port number.



