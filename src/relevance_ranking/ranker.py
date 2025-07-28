# src/relevance_ranking/ranker.py

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_sections(sections, persona, job):
    query = f"{persona} needs to {job}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    section_embeddings = model.encode(sections, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, section_embeddings)[0]

    ranked = sorted(
        [
            {"text": sec, "score": float(score), "rank": i + 1}
            for i, (sec, score) in enumerate(
                sorted(zip(sections, scores), key=lambda x: -x[1])
            )
        ],
        key=lambda x: x["rank"]
    )

    return ranked, ranked[:3]  # top 3 sections (optional)
