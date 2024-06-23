# Използване на официалния Python образ като базов
FROM python:3.9

# Създаване на директория за приложението
WORKDIR /app

# Копиране на зависимостите и кода в контейнера
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY model.py model.py
COPY model.pkl model.pkl

# Инсталиране на зависимостите
RUN pip install --no-cache-dir -r requirements.txt

# Излагане на порта, на който ще слуша приложението
EXPOSE 5000

# Стартиране на приложението
CMD ["python", "app.py"]
