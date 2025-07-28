import re
from langdetect import detect

def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()

def infer_heading_level(font_size, flags=0):
    if font_size > 18:
        return "H1"
    elif font_size > 14:
        return "H2"
    elif font_size > 11:
        return "H3"
    return None

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"