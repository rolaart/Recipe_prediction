from flask import Flask, request, jsonify
from model import load_model, predict, last_special_request_time
import traceback
from datetime import datetime

app = Flask(__name__)

model = load_model()

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
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

@app.route('/request_special', methods=['POST'])
def request_special():
    global last_special_request_time
    last_special_request_time = datetime.now()
    return jsonify({'status': 'Special recipes will be included for the next 24 hours'}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
