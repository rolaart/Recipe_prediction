from flask import Flask, request, jsonify
from model import load_model, predict
import traceback

app = Flask(__name__)

# Зареждане на модела при стартиране на приложението
model = load_model()

@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Проверка за наличието на необходимите параметри
        if 'input' not in data:
            return jsonify({'error': 'Missing "input" parameter'}), 400
        
        input_data = data['input']
        prediction = predict(model, input_data)
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
