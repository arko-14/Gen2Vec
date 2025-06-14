FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get upgrade -y && apt-get install --no-install-recommends -y gcc && \
	pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt && \
	apt-get purge -y --auto-remove gcc && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY app ./app
COPY data ./data
COPY credentials.json ./credentials.json
EXPOSE 5000
CMD ["python", "app/app.py"]