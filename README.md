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
```
#### 2. For Advice (low status)
```python
response = requests.get(
    "http://localhost:8000",
    params={"status": "low", "nutrient": "iron"}
)
```
#### 3.For Motivation (goal-based)
```python
response = requests.get(
    "http://localhost:8000",
    params={"goal": "muscle_gain"}
)
```
### How to RECEIVE Data
#### Success Response (200 OK)
```python
{
    "quote": "Your iron levels are low. Try eating more spinach!",
    "type": "advice",
    "timestamp": "2025-08-05T12:00:00Z"
}
```
#### Error Response (400 Bad Request)
```python
{
    "error": "Missing parameters",
    "message": "Provide either status+nutrient or goal",
    "timestamp": "2025-08-05T12:00:00Z"
}
```
