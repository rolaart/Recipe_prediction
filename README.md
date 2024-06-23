# Recipe Recommendation System

This is a Flask-based API for recommending recipes. The system can suggest recipes based on the last time they were cooked, the season, and user feedback.

## Requirements

- Docker
- Docker Compose (optional)
- pytest (for running tests)

## Building and Running the Docker Container

1. Clone the repository:

    ```bash
    git clone https://github.com/YOUR_USERNAME/recipe-recommendation-system.git
    cd recipe-recommendation-system
    ```

2. Build the Docker image:

    ```bash
    docker build -t recommendation-system .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 5000:5000 recommendation-system
    ```

4. The API will be available at `http://localhost:5000`.

## API Endpoints

### Predict Recipes

- **Endpoint**: `/predict`
- **Method**: `POST`
- **Description**: Predict recipes based on provided data and average temperature.

- **Request Body**:
    ```json
    {
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
          "special": true
        },
        {
          "name": "Recipe 3",
          "last_cooked_date": "2023-11-20",
          "season": "fall"
        },
        {
          "name": "Recipe 4",
          "last_cooked_date": "2024-04-12",
          "expensive": true
        }
      ],
      "avg_temp": 25,
      "include_special": true
    }
    ```

- **Response Body**:
    ```json
    {
      "prediction": [
        {
          "name": "Recipe 3",
          "last_cooked_date": "2023-11-20",
          "season": "fall",
          "drink_recommendation": "With this recipe a good addition would be: a cold drink",
          "adjusted_score": 4.5
        },
        ...
      ]
    }
    ```

### Add Recipe

- **Endpoint**: `/add_recipe`
- **Method**: `POST`
- **Description**: Add a new recipe.

- **Request Body**:
    ```json
    {
      "name": "Recipe 5",
      "last_cooked_date": "2024-06-01",
      "season": "summer",
      "expensive": true,
      "special": false
    }
    ```

- **Response Body**:
    ```json
    {
      "status": "Recipe added successfully",
      "recipe": {
        "name": "Recipe 5",
        "last_cooked_date": "2024-06-01",
        "season": "summer",
        "expensive": true,
        "special": false
      }
    }
    ```

### Submit Feedback

- **Endpoint**: `/submit_feedback`
- **Method**: `POST`
- **Description**: Submit feedback for a recipe.

- **Request Body**:
    ```json
    {
      "recipe_name": "Recipe 1",
      "rating": 4
    }
    ```

- **Response Body**:
    ```json
    {
      "status": "Feedback submitted successfully"
    }
    ```

### Request Special Recipes

- **Endpoint**: `/request_special`
- **Method**: `POST`
- **Description**: Request that special recipes be included in recommendations for the next 24 hours.

- **Response Body**:
    ```json
    {
      "status": "Special recipes will be included for the next 24 hours"
    }
    ```

### Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Check if the service is running.

- **Response Body**:
    ```json
    {
      "status": "ok"
    }
    ```

## Running Tests

To run the tests for the API and model, follow these steps:

1. Install `pytest` and `requests` if you haven't already:

    ```bash
    pip install pytest requests
    ```

2. Make sure your Docker container is running:

    ```bash
    docker run -p 5000:5000 recommendation-system
    ```

3. Run the tests:

    ```bash
    pytest test_app.py
    pytest test_model.py
    ```

### Test Files

**test_app.py**
**test_model.py**
