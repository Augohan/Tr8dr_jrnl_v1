import sys
from image_processing import preprocess_image
from ocr_extraction import extract_text
from llm_integration import generate_insights
from trade_journal_formatter import format_journal_entry

def main(image_path):
    preprocessed_image = preprocess_image(image_path)
    extracted_text = extract_text(preprocessed_image)

    # Example mock data
    prices = {"entry": 120, "last_price": 122, "chg_percent": 1.67}
    entry_dna = "Taking incremental profits"

    insights = generate_insights(extracted_text, prices, entry_dna)
    # Format and print the journal entry
        journal_entry = TradeJournalEntry(
        ticker="CPT",
        entry_price=prices['entry'],
        last_price=prices['last_price'],
        change_percent=prices['chg_percent'],
        entry_dna=entry_dna,
        comments=extracted_text,
        dca_level=110,
        llm_insights=insights
     )


    print(journal_entry)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
    else:
        main(sys.argv[1])
