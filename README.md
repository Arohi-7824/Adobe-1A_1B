# 🧠 PDF Outline Extractor – Hackathon Round 1A

## 🔍 What It Does
- Takes PDFs from `/app/input`
- Extracts:
  - Title (from metadata or filename)
  - Headings: H1, H2, H3 based on font size
  - Page numbers for each heading
- Outputs JSON to `/app/output`

## ⚙️ Build and Run

### Build the Docker Image
```bash
docker build --platform linux/amd64 -t pdfextractor:solution1a .
