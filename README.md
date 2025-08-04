# Quote Generator Microservice

## Communication Contract

### How to REQUEST Data
Make GET requests to the root endpoint `/` with these parameters:

#### 1. For Praise (excellent status)
```python
import requests
response = requests.get(
    "http://localhost:8000",
    params={"status": "excellent", "nutrient": "protein"}
)
