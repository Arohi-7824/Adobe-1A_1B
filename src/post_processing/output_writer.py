import json
import os

def write_json(pdf_path, title, outline, persona, job):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = f"output/{base_name}.json"

    json.dump({
        "title": title,
        "outline": outline,
        "persona": persona,
        "job": job
    }, open(output_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)