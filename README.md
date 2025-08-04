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

<img width="1713" height="1293" alt="UML" src="https://github.com/user-attachments/assets/690b0a51-c1c3-4b95-b0fc-8c302586f55d" />
