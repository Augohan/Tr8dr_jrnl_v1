import unittest
from src.ocr_extraction import extract_text

class TestOCRExtraction(unittest.TestCase):
    def test_extract_text(self):
        # Add test cases for OCR extraction
        self.assertIsNotNone(extract_text("path/to/test/image.png"))

if __name__ == '__main__':
    unittest.main()
