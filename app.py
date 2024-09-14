from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Configure the Google Generative AI API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  # Use environment variable for API key
if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/analyze', methods=['POST'])
def analyze_time_complexity():
    data = request.get_json()
    print(f"Received data: {data}")  # Log received data
    code = data.get('code', '')  # Get the code from the request

    if not code:
        return jsonify({"result": "No code provided"}), 400

    try:
        model = genai.GenerativeModel('gemini-pro')  # Verify this method
        response = model.generate_content(f"Analyze the time complexity: {code}. Important: don't give any additional statements, just give time complexity.")
        
        if response and response.text:
            return jsonify({"result": response.text}), 200
        else:
            return jsonify({"result": "No response from AI model"}), 500

    except Exception as e:
        print(f"Error during API call: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # Specify host and port
