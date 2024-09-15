from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Configure the Google Generative AI API key
GOOGLE_API_KEY = 'AIzaSyBxb1ughJXCz6M9hb7bxlal7ZnfWrNdzAk'  # Use environment variable for API key
if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/analyze/time', methods=['POST'])
def analyze_time_complexity():
    data = request.get_json()
    code = data.get('code', '')  # Get the code from the request

    if not code:
        return jsonify({"result": "No code provided"}), 400

    try:
        # Generate the time complexity analysis
        model = genai.GenerativeModel("gemini-1.5-flash")  # Verify that this is the correct method
        response = model.generate_content(f"Analyze the time complexity: {code}. Important: don't give any additional statements, just give time complexity.")
        
        if response and response.text:
            return jsonify({"result": response.text}), 200
        else:
            return jsonify({"result": "No response from AI model"}), 500

    except Exception as e:
        print(f"Error during API call: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route('/analyze/memory', methods=['POST'])
def analyze_memory_taken():
    data = request.get_json()
    code = data.get('code', '')  # Get the code from the request

    if not code:
        return jsonify({"result": "No code provided"}), 400

    try:
        # Generate the time complexity analysis
        model = genai.GenerativeModel("gemini-1.5-flash")  # Verify that this is the correct method
        response = model.generate_content(f"Analyze the Memory taken in big oh terms: {code}. Important: don't give any additional statements, just give memory taken.")
        
        if response and response.text:
            return jsonify({"result": response.text}), 200
        else:
            return jsonify({"result": "No response from AI model"}), 500

    except Exception as e:
        print(f"Error during API call: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # Specify host and port
