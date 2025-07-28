import re
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.utils import clean_text, infer_heading_level

def detect_headings(blocks, lang):
    headings = []
    max_font = 0
    title_candidate = ""

    vectorizer = TfidfVectorizer(max_features=500)
    tfidf = vectorizer.fit_transform(blocks)

    for i, text in enumerate(blocks):
        cleaned = clean_text(text)
        if not cleaned or len(cleaned.split()) > 20:
            continue

        font_size = 12 + (tfidf[i].nnz % 8)  # Fake heuristic
        if font_size > max_font and len(cleaned.split()) > 2:
            max_font = font_size
            title_candidate = cleaned

        heading_level = infer_heading_level(font_size)
        if heading_level:
            headings.append({
                "level": heading_level,
                "text": cleaned,
                "page": i + 1
            })

    return title_candidate, headings