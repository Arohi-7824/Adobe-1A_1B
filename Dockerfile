FROM python:3.10-slim

# Avoid interactive prompts + reduce image size
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y gcc git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Pre-copy requirements only to cache this step
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy actual code
COPY . .

CMD ["python", "src/main.py"]
