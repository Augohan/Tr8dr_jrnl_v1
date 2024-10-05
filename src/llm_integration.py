import openai

def generate_insights(extracted_data):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": extracted_data}]
    )
    return response.choices[0].message['content']
