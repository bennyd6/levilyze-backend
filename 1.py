import os
import google.generativeai as genai

# Set your API key here or use environment variable
api_key = os.getenv('GOOGLE_API_KEY')  # Make sure this key is correct
if not api_key:
    raise ValueError("API key is not set.")

genai.configure(api_key=api_key)

# Test if the API works
try:
    model = genai.GenerativeModel("gemini-1.5-flash")  # Replace with the correct model name
    response = model.generate_content("What is the capital of France?")
    print("API Response:", response.text)
except Exception as e:
    print("Error during API call:", e)
