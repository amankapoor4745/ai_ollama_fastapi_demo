import os
# test_api.py
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("Ollama_API_KEY")
url = "http://127.0.0.1:8000/ask"  # must match server endpoint

data = {
    "query": "Who is the PM of India",
    "api_key": API_KEY
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)