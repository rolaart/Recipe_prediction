import pickle

def load_model():
    # Зареждане на предварително обучен модел от файл
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model, input_data):
    # Предсказване на резултатите с модела
    # Очакваме input_data да е в подходящ формат (например списък)
    result = model.predict([input_data])
    return result.tolist()
