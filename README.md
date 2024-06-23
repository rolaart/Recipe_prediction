# Recipe_prediction


Instructions to building and start of the container:
  1. docker build -t recommendation-system
  2. docker run -p 5000:5000 recommendation-system

Testing:
Sample bash run:
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d 'testing/example.json'
```

Special bash run:
```
curl -X POST http://localhost:5000/request_special
```
