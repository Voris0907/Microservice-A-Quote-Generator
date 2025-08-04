# Microservice-A-Quote-Generator

## Communication Contract

### How to REQUEST Data
Make GET requests to the root endpoint `/` with these parameters:

**For Praise (excellent status):**
```python
import requests
response = requests.get(
    "http://localhost:8000",
    params={"status": "excellent", "nutrient": "protein"}
)

**For Advice (low status):**
```python
response = requests.get(
    "http://localhost:8000",
    params={"status": "low", "nutrient": "iron"}
)
