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
For Advice (low status):

python
response = requests.get(
    "http://localhost:8000",
    params={"status": "low", "nutrient": "iron"}
)
For Motivation (goal-based):

python
response = requests.get(
    "http://localhost:8000",
    params={"goal": "muscle_gain"}
)
How to RECEIVE Data
Success Response (200 OK):

json
{
    "quote": "Your iron levels are low. Try eating more spinach!",
    "type": "advice",
    "timestamp": "2025-08-05T12:00:00Z"
}
Error Response (400 Bad Request):

json
{
    "error": "Missing parameters",
    "message": "Provide either status+nutrient or goal",
    "timestamp": "2025-08-05T12:00:00Z"
}
UML Sequence Diagram
<img width="1713" height="1293" alt="UML" src="https://github.com/user-attachments/assets/690b0a51-c1c3-4b95-b0fc-8c302586f55d" />
