from flask import Flask, request, jsonify
from model import load_model, predict, last_special_request_time, submit_feedback, adjust_recommendations
import traceback
from datetime import datetime

app = Flask(__name__)

model = load_model()
recipes_db = []

@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        data = request.json
        if not data or 'recipes' not in data or 'avg_temp' not in data:
            return jsonify({'error': 'No data, "recipes" or "avg_temp" parameter provided'}), 400
        
        recipes = data['recipes']
        avg_temp = data['avg_temp']
        include_special = data.get('include_special', False)
        prediction = predict(model, recipes, avg_temp, include_special)
        
        # Адаптиране на препоръките въз основа на обратната връзка
        prediction = adjust_recommendations(prediction)
        
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

@app.route('/request_special', methods=['POST'])
def request_special():
    global last_special_request_time
    last_special_request_time = datetime.now()
    return jsonify({'status': 'Special recipes will be included for the next 24 hours'}), 200

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    try:
        data = request.json
        required_fields = ['name', 'last_cooked_date']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        new_recipe = {
            'name': data['name'],
            'last_cooked_date': data['last_cooked_date'],
            'season': data.get('season', ''),
            'expensive': data.get('expensive', False),
            'special': data.get('special', False)
        }

        recipes_db.append(new_recipe)
        return jsonify({'status': 'Recipe added successfully', 'recipe': new_recipe}), 201
    
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback_route():
    try:
        data = request.json
        if not data or 'recipe_name' not in data or 'rating' not in data:
            return jsonify({'error': 'No data, "recipe_name" or "rating" parameter provided'}), 400
        
        recipe_name = data['recipe_name']
        rating = data['rating']
        submit_feedback(recipe_name, rating)
        return jsonify({'status': 'Feedback submitted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
