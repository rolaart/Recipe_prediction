import pytest
from model import load_model, predict, submit_feedback, adjust_recommendations

@pytest.fixture(scope='module')
def model():
    return load_model()

def test_load_model(model):
    assert model is not None

def test_predict(model):
    recipes = [
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
    ]
    avg_temp = 25
    include_special = True
    predictions = predict(model, recipes, avg_temp, include_special)
    assert len(predictions) > 0
    assert "drink_recommendation" in predictions[0]

def test_submit_feedback():
    recipe_name = "Recipe 1"
    rating = 4
    submit_feedback(recipe_name, rating)
    # Проверка дали обратната връзка е добавена правилно
    from model import feedback
    assert len(feedback) > 0
    assert feedback[-1] == {'recipe_name': recipe_name, 'rating': rating}

def test_adjust_recommendations():
    recipes = [
        {"name": "Recipe 1", "last_cooked_date": "2024-01-10"},
        {"name": "Recipe 2", "last_cooked_date": "2023-06-15"}
    ]
    submit_feedback("Recipe 1", 5)
    submit_feedback("Recipe 2", 3)
    adjusted_recipes = adjust_recommendations(recipes)
    assert adjusted_recipes[0]['name'] == "Recipe 1"
    assert adjusted_recipes[1]['name'] == "Recipe 2"
