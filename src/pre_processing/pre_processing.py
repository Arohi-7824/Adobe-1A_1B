import fitz
from utils.utils import clean_text, detect_language

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []
    all_text = ""

    for page in doc:
        text = page.get_text("text")
        all_text += text
        for b in page.get_text("blocks"):
            blocks.append(b[4])  # block text

    lang = detect_language(all_text)
    return blocks, lang