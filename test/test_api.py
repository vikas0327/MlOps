# Import TestClient so we can send simulated HTTP request directly to FastAPI
from fastapi.testclient import TestClient

# import the application object defined in main.py
from main import app

# Create a reusable test client for all test functions.
client = TestClient(app)

def test_health_endpoint():
    '''
    Verify that the application is running and can respond to a health-check request
    '''
    response = client.get("/health")
    # A successful HTTP request should return status code 200
    assert response.status_code == 200

    #Now check response body
    assert response.json() =={"status":"healthy"}

def test_valid_iris_prediction():
    '''
    Verify that valid flower measurement produce a preediction
    '''
    payload={
        "sepal_length":2.6,
        "sepal_width":2.4,
        "petal_length":1.2,
        "petal_width":1.1
    }

    # send a simulated HTTP POST request with JSON iinput
    response = client.post("/predict",json=payload)
    assert response.status_code ==200
    # convert the json response into a python Dictionary
    result = response.json()

    # check the response contarct: both field must exist
    assert "prediction" in result
    assert "class_name" in result

    # The predicted class must be one of the three iris classes
    assert result["class_name"] in ["setosa","versicolor","virginica"]
    assert result["prediction"] in [0,1,2]

def test_invalid_iris_input():
    ''' verify that invalid inputs are rejeted by fastapi
    '''
    payload ={
        "sepal_length":-2.6,
        "sepal_width":2.4,
        "petal_length":1.2,
        "petal_width":1.1
    }
    response=client.post("/predict",json=payload)
    assert response.status_code == 422