import requests

def test_requests():
    base_url = "http://localhost:8000"
    test_cases = [
        {"name": "Praise - Excellent Protein", "params": {"status": "excellent", "nutrient": "protein"}},
        {"name": "Advice - Low Iron", "params": {"status": "low", "nutrient": "iron"}},
        {"name": "Motivation - Muscle Gain", "params": {"goal": "muscle_gain"}},
        {"name": "Error - Missing Params", "params": {}}
    ]
    
    for test in test_cases:
        print(f"\n[TEST] {test['name']}")
        print(f"Request: {test['params']}")
        
        try:
            response = requests.get(base_url, params=test["params"])
            print(f"Status: {response.status_code}")
            print("Response:", response.json())
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_requests()
