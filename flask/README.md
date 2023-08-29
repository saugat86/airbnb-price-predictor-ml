## Flask App

### Install

Create a virtual environment.

```cmd
python -m venv venv
source venv\Scripts\activate
```

Install the necessary libraries.

```
pip install -r requirements.txt
```

#### Local Run

In the top level of the directory of airbnb_app fire up a terminal and execute:

```cmd
python app.py
```

### Code Structure

#### Top level

- app.py: Applications entrypoint. Used to start the webserver. Here we register our blueprints
- airbnb_base_logger.py: Logger for incoming information

#### Controllers

One file per logical unit:

- ping: Typical ping endpoint.
- stats: Declares the endpoint where we can request the statistics.
- models: Accepts data for an individual listing and return a predicted price.
- airbnb: Supports basic HTTP requests. GET, POST, DELETE an airbnb based on id.

#### Repo

The data storage of the application. Should include the airbnb.csv initially.
In case you delete or update something on the dataset, you can always replace
it with the original_airbnb_copy.csv and bring it to its original state.

#### Services

The business logic of our app.

- stats: Functions that calculate several stats based on aggregations by utilized the pandas lib.
- aibnb: Mappings, utilities and anything else needed to work with the airbnb resource.

#### Test

Tests for the app.

```
python -m pytest
```

- Execute stress tests

Run

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
