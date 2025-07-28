import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import os

def extract_text_from_image(image_path, lang='eng'):
    """
    Extracts text from a single image file using Tesseract OCR.
    
    Parameters:
    - image_path (str): Path to the image.
    - lang (str): Language code for OCR (e.g., 'eng', 'jpn').

    Returns:
    - str: Extracted text.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=lang)
        return text
    except Exception as e:
        print(f"[✘] OCR failed on {image_path}: {e}")
        return ""


def extract_text_from_pdf(pdf_path, lang='eng'):
    """
    Converts PDF pages to images and performs OCR on each page.

    Parameters:
    - pdf_path (str): Path to the PDF file.
    - lang (str): Language code for OCR.

    Returns:
    - list of str: Text content of each page.
    """
    try:
        doc = fitz.open(pdf_path)
        texts = []

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=300)
            img_path = f"/tmp/page_{page_num}.png"
            pix.save(img_path)

            text = extract_text_from_image(img_path, lang=lang)
            texts.append(text)

            os.remove(img_path)  # Cleanup temp image

        return texts

    except Exception as e:
        print(f"[✘] OCR failed for PDF {pdf_path}: {e}")
        return []
