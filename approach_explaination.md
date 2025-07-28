Approach Explanation for Intelligent Document Analyst
The intelligent document analyst extends the existing PDF outline extractor to extract and prioritize relevant sections from 3–10 PDFs based on a persona and job-to-be-done. The solution uses pdfplumber==0.11.4 for text extraction, ensuring a lightweight footprint (<50MB) and offline operation on CPU (AMD64). Processing time is optimized to handle 3–5 documents in <60 seconds.
Methodology

Input Processing:

A JSON file (input.json) specifies the document list, persona, and job-to-be-done. The main.py script reads this file and processes all PDFs in the input directory.


Text Extraction:

pdf_processor.py extracts text from each PDF page using pdfplumber. It identifies headings (H1, H2, H3) based on font size (relative to page average), boldness, and y-position (top 10% of page). Text under each heading is collected as subsection content, preserving Unicode for multilingual support (e.g., Japanese, Hindi, English).


Relevance Ranking:

A keyword-based scoring mechanism prioritizes sections. Keywords are derived from the job-to-be-done (e.g., "methodologies," "datasets" for a PhD researcher). Each section’s text is scored using term frequency (TF) of keywords, weighted by heading level (H1: 1.5, H2: 1.2, H3: 1.0). The top 10 sections are ranked by score.


Subsection Analysis:

Text under each heading is cleaned (removing (cid:XX) codes, short/empty lines) and summarized by extracting the first 100 characters to provide concise subsection content.


Output Generation:

The output JSON includes metadata (documents, persona, job, timestamp), extracted sections (document, page, title, importance rank), and subsection analysis (document, refined text, page). Results are written to output/output.json.



Implementation Details

utils.py: Enhanced with keyword extraction (simple tokenization) and scoring functions. Stricter text validation excludes CID fonts and invalid text.
pdf_processor.py: Extracts headings and subsections, computes relevance scores, and formats output.
main.py: Orchestrates processing of multiple PDFs based on input.json.
Constraints: Uses pdfplumber only, ensuring <1GB size. Optimized for speed by limiting text processing to lightweight operations. Runs offline, handling multilingual PDFs via Unicode.

This approach generalizes to diverse domains (research papers, textbooks, reports), personas (researcher, student, analyst), and jobs (literature review, exam prep, financial analysis) by relying on flexible, keyword-driven relevance ranking.