import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_sections(sections, persona_text, job_text, top_k=5):
    documents = [persona_text + " " + job_text] + [s["text"] for s in sections]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform(documents)

    query_vec = tfidf[0]
    doc_vecs = tfidf[1:]

    scores = cosine_similarity(query_vec, doc_vecs).flatten()

    for i, section in enumerate(sections):
        section["relevance_score"] = float(scores[i])

    top_sections = sorted(sections, key=lambda x: x["relevance_score"], reverse=True)[:top_k]
    return sections, top_sections
