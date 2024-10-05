import pytesseract

def extract_text(image):
    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text
