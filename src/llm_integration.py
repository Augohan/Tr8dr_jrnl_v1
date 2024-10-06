import openai
import os  # Import the os module to access environment variables

# Access the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY_TR8D_JRNL")

def generate_insights(extracted_text, prices, dna):
    """
    Get trade insights from GPT based on extracted text, prices, and entry DNA.
    """
    prompt = f"""
    You are a trading assistant. Based on the following extracted data from a trading chart:
    - Extracted Text: {extracted_text}
    - Prices: {prices}
    - Entry DNA: {dna}
    
    Provide a summarized trading strategy, key insights, and next steps.
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # or use GPT-4 if available
        prompt=prompt,
        max_tokens=150
    )
    
    insights = response.choices[0].text.strip()
    return insights

# Example usage
if __name__ == "__main__":
    sample_extracted_text = "Taking profits after a 5.85% move."
    sample_prices = {"entry": 120, "last_price": 122, "chg_percent": 1.67}
    sample_dna = "Incremental profits"
    
    trade_insights = get_trade_insights(sample_extracted_text, sample_prices, sample_dna)
    print(f"Trade Insights: {trade_insights}")
