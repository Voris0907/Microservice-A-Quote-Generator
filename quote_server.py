from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import json
import urllib.parse as urlparse

class QuoteHandler(BaseHTTPRequestHandler):
    FOOD_MAP = {"iron": "spinach", "protein": "lean meats", "vitamin c": "oranges"}
    GOAL_QUOTES = {
        "muscle_gain": "Every rep counts! Your muscles are getting stronger!",
        "weight_loss": "Small steps lead to big results! Stay consistent!"
    }

    def do_GET(self):
        params = urlparse.parse_qs(urlparse.urlparse(self.path).query)
        response = {}
        
        try:
            if 'status' in params and 'nutrient' in params:
                status = params['status'][0].lower()
                nutrient = params['nutrient'][0]
                
                if status == "excellent":
                    response = self._generate_praise(nutrient)
                elif status == "low":
                    response = self._generate_advice(nutrient)
                else:
                    raise ValueError("Status must be 'excellent' or 'low'")
                    
            elif 'goal' in params:
                response = self._generate_motivation(params['goal'][0])
            else:
                raise ValueError("Require either status+nutrient or goal")
                
        except Exception as e:
            response = {"error": str(e), "timestamp": datetime.now().isoformat()}
            self.send_response(400)
        else:
            self.send_response(200)
            
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def _generate_praise(self, nutrient):
        return {
            "quote": f"Great job on your {nutrient} intake! Keep it up!",
            "type": "praise",
            "timestamp": datetime.now().isoformat()
        }
    
    def _generate_advice(self, nutrient):
        food = self.FOOD_MAP.get(nutrient.lower(), "healthy foods")
        return {
            "quote": f"Your {nutrient} levels are low. Try eating more {food}!",
            "type": "advice",
            "timestamp": datetime.now().isoformat()
        }
    
    def _generate_motivation(self, goal):
        return {
            "quote": self.GOAL_QUOTES.get(goal, "Stay focused on your goals!"),
            "type": "motivation",
            "timestamp": datetime.now().isoformat()
        }

def run(port=8000):
    server = HTTPServer(('', port), QuoteHandler)
    print(f"Server running on http://localhost:{port}")
    server.serve_forever()

if __name__ == "__main__":
    run()
