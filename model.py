import pickle
import pandas as pd
from datetime import datetime, timedelta

# Глобална променлива за време на последна заявка за скъпи/специални рецепти
last_special_request_time = None

def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model, recipes, avg_temp, include_special=False):
    today = datetime.now()
    season = get_season(today)
    
    global last_special_request_time
    if include_special:
        last_special_request_time = today
    
    include_special_recipes = False
    if last_special_request_time:
        if today - last_special_request_time < timedelta(hours=24):
            include_special_recipes = True

    # Филтриране на рецепти
    filtered_recipes = []
    for recipe in recipes:
        if not include_special_recipes and ('expensive' in recipe or 'special' in recipe):
            continue
        
        last_cooked_date = datetime.strptime(recipe['last_cooked_date'], '%Y-%m-%d')
        if 'season' in recipe and recipe['season'] != season:
            continue
        days_since_last_cooked = (today - last_cooked_date).days
        filtered_recipes.append((days_since_last_cooked, recipe))
    
    filtered_recipes.sort(reverse=True, key=lambda x: x[0])
    
    recommendations = [recipe[1] for recipe in filtered_recipes]
    
    drink_type = get_drink_recommendation(avg_temp)
    for recommendation in recommendations:
        recommendation["drink_recommendation"] = f"With this recipe a good addition would be: {drink_type}"
    
    return recommendations

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

def get_drink_recommendation(avg_temp):
    if avg_temp >= 20:
        return "a cold drink"
    else:
        return "a hot drink"
