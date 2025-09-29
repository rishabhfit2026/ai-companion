import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    print("API Key configured successfully.")
except Exception as e:
    print(f"Error configuring API Key: {e}")
    exit()

print("\nAvailable models for your API key:")
print("-" * 30)

try:
    # List all models that support the "generateContent" method
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"\nCould not list models. Error: {e}")

print("-" * 30)
print("\nPlease copy the full output of this script and share it.")

