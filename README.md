# Quote Generator Microservice

## API Communication Contract

### Requesting Data
```python
import requests

# For praise (excellent status)
response = requests.get(
    "http://localhost:8000",
    params={"status": "excellent", "nutrient": "protein"}
)

# For advice (low status)
response = requests.get(
    "http://localhost:8000", 
    params={"status": "low", "nutrient": "iron"}
)

# For motivation (goal-based)
response = requests.get(
    "http://localhost:8000",
    params={"goal": "muscle_gain"}
)
