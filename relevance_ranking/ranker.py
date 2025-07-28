from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_sections(sections, persona_text, job_text, top_k=5):
    documents = [persona_text + " " + job_text] + sections
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(documents)
    
    similarities = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()
    ranked_indices = similarities.argsort()[::-1][:top_k]
    
    return [(sections[i], similarities[i]) for i in ranked_indices]
