from flask import Flask, request, jsonify
from model import load_model, predict
import traceback

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
        prediction = predict(model, recipes, avg_temp)
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
