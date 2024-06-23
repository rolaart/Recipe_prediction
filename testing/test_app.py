import pytest
import requests
from datetime import datetime, timedelta

BASE_URL = "http://localhost:5000"

@pytest.fixture(scope='module')
def start_server():
    # Here you can start the server if it's not running
    # and stop it after the tests
    yield
    # Here you can stop the server if needed

def test_health_check(start_server):
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_add_recipe(start_server):
    recipe = {
        "name": "Recipe Test",
        "last_cooked_date": "2024-06-01",
        "season": "summer",
        "expensive": True,
        "special": False
    }
    response = requests.post(f"{BASE_URL}/add_recipe", json=recipe)
    assert response.status_code == 201
    assert response.json()['status'] == "Recipe added successfully"

def test_predict(start_server):
    data = {
      "recipes": [
        {
          "name": "Recipe 1",
          "last_cooked_date": "2024-01-10",
          "season": "winter"
        },
        {
          "name": "Recipe 2",
          "last_cooked_date": "2023-06-15",
          "season": "summer",
          "special": True
        },
        {
          "name": "Recipe 3",
          "last_cooked_date": "2023-11-20",
          "season": "fall"
        },
        {
          "name": "Recipe 4",
          "last_cooked_date": "2024-04-12",
          "expensive": True
        }
      ],
      "avg_temp": 25,
      "include_special": True
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 200
    predictions = response.json().get('prediction', [])
    assert len(predictions) > 0
    assert "drink_recommendation" in predictions[0]

def test_submit_feedback(start_server):
    feedback = {
      "recipe_name": "Recipe 1",
      "rating": 4
    }
    response = requests.post(f"{BASE_URL}/submit_feedback", json=feedback)
    assert response.status_code == 200
    assert response.json()['status'] == "Feedback submitted successfully"

def test_request_special(start_server):
    response = requests.post(f"{BASE_URL}/request_special")
    assert response.status_code == 200
    assert response.json()['status'] == "Special recipes will be included for the next 24 hours"
