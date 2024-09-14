from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Configure the Google Generative AI API key
GOOGLE_API_KEY = 'AIzaSyBxb1ughJXCz6M9hb7bxlal7ZnfWrNdzAk'
genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/analyze', methods=['POST'])
def analyze_time_complexity():
    data = request.get_json()
    code = data.get('code', '')  # Get the code from the request

    if not code:
        return jsonify({"result": "No code provided"}), 400

    try:
        # Generate the time complexity analysis
        model = genai.GenerativeModel('gemini-pro')  # Verify that this is the correct method
        response = model.generate_content(f"Analyze the time complexity: {code}. Important: don't give any additional statements, just give time complexity.")
        
        if response and response.text:
            return jsonify({"result": response.text}), 200
        else:
            return jsonify({"result": "No response from AI model"}), 500

    except Exception as e:
        print(f"Error during API call: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
