import pickle
import pandas as pd
from datetime import datetime, timedelta

def load_model():
    # Примерен модел - в реален сценарий може да бъде по-сложен модел за препоръки
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model, recipes):
    today = datetime.now()
    season = get_season(today)
    
    # Филтриране на рецепти, които не са приготвяни дълго време и са в сезона
    filtered_recipes = []
    for recipe in recipes:
        last_cooked_date = datetime.strptime(recipe['last_cooked_date'], '%Y-%m-%d')
        if 'season' in recipe and recipe['season'] != season:
            continue
        days_since_last_cooked = (today - last_cooked_date).days
        filtered_recipes.append((days_since_last_cooked, recipe))
    
    # Сортиране по най-дълго време неприготвяни
    filtered_recipes.sort(reverse=True, key=lambda x: x[0])
    
    # Връщане на сортиран списък от препоръчани рецепти
    return [recipe[1] for recipe in filtered_recipes]

def get_season(date):
    month = date.month
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    else:
        return 'fall'
