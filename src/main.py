import sys
from image_processing import preprocess_image
from ocr_extraction import extract_text
from llm_integration import generate_insights
from trade_journal_formatter import format_journal_entry

def main(image_path):
    preprocessed_image = preprocess_image(image_path)
    extracted_text = extract_text(preprocessed_image)
    insights = generate_insights(extracted_text)
    # Format and print the journal entry
    journal_entry = format_journal_entry("AAPL", 150, 155, 3.33, insights)
    print(journal_entry)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
    else:
        main(sys.argv[1])
