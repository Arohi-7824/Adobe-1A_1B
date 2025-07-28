import sys
import os

# Ensure src is on the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from pre_processing.pdf_loader import get_pdf_files
from pre_processing.pre_processing import extract_text_blocks
from extractor.heading_detector import detect_headings
from post_processing.output_writer import write_json
from relevance_ranking.ranker import rank_sections  # You must create this

# Load persona and job-to-be-done
with open("persona.txt", "r", encoding="utf-8") as f:
    persona = f.read().strip()

with open("job.txt", "r", encoding="utf-8") as f:
    job = f.read().strip()

# Process all PDFs in the input folder
pdf_paths = get_pdf_files("input")

for pdf_path in pdf_paths:
    # Extract blocks and language
    blocks, lang = extract_text_blocks(pdf_path)

    # Detect headings and outline
    title, outline = detect_headings(blocks, lang)

    # Prepare sections for relevance ranking
    section_texts = [section['text'] for section in outline if 'text' in section]

    # Rank sections based on persona and job
    ranked_sections, _ = rank_sections(section_texts, persona, job)

    # Add ranking info back to outline
    ranked_outline = []
    for i, section in enumerate(outline):
        if 'text' in section:
            section['score'] = ranked_sections[i]['score']
            section['rank'] = ranked_sections[i]['rank']
        ranked_outline.append(section)

    # Write output
    write_json(pdf_path, title, ranked_outline, persona, job)

