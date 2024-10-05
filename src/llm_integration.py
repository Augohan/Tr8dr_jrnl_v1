import openai
import os  # Import the os module to access environment variables

# Access the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY_TR8D_JRNL")

def generate_insights(extracted_data):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": extracted_data}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        return "No insights available."
