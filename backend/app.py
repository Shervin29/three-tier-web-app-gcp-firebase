from flask import Flask
from flask_cors import CORS
import os

print("Flask app starting...")
app = Flask(__name__)
CORS(app)
print("Flask app instance created.")

@app.route('/')
def hello():
    return "Hello from Backend!"

if __name__ == '__main__':
    print("Running in __main__ block.")
    port = int(os.environ.get("PORT", 8080))
    print(f"Attempting to run app on host=0.0.0.0, port={port}")
    app.run(debug=True, host='0.0.0.0', port=port)
    print("App finished running (shouldn't see this in normal operation).")