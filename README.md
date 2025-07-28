PDF Outline & Relevance Extractor
This tool extracts structured outlines (Title, H1–H3) from PDFs and ranks the most relevant sections based on a user persona and job-to-be-done. It supports multilingual documents and runs efficiently in CPU-only environments.

Features
  - Detects document title and headings (H1, H2, H3) using heuristics and optional ML.

  - Supports multilingual PDFs (e.g., English, Japanese).

  - Ranks top sections using semantic similarity to persona.txt and job.txt.

  - Outputs structured JSON per PDF.

Input
PDFs: Place in input/

Text files:

  - persona.txt: User background and goals
  - job.txt: Desired task or objective

Output
JSON per file in output/, containing:

Extracted outline
Top relevant sections

Run Locally

  - pip install -r requirements.txt
  - python src/main.py

Run with Docker

  - docker build -t pdf-processor .
  - docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-processor