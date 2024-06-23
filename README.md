# Recipe_prediction


Instructions to building and start of the container:
  1. docker build -t recommendation-system
  2. docker run -p 5000:5000 recommendation-system

Testing:
In bash run:
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{
  "recipes": [
    {
      "name": "Recipe 1",
      "last_cooked_date": "2024-01-10",
      "season": "winter"
    },
    {
      "name": "Recipe 2",
      "last_cooked_date": "2023-06-15",
      "season": "summer"
    },
    {
      "name": "Recipe 3",
      "last_cooked_date": "2023-11-20",
      "season": "fall"
    },
    {
      "name": "Recipe 4",
      "last_cooked_date": "2024-04-12"
    }
  ],
  "avg_temp": 25
}'
```
