# Gen2Vec


---

# 🚀 Dockerized ML Service with LLM-based Data Generation & Vector Embedding using Qdrant

This project demonstrates a **containerized machine learning service** that:

* Generates synthetic data using a **Large Language Model (LLM)**
* Saves the generated data as a **CSV file**
* Converts the text into **embeddings**
* Stores the embeddings into a **local vector database (Qdrant)**
* All of this is wrapped in a **Dockerized pipeline** using `docker-compose`.

---

## 🧠 Why These Choices?

### ✅ LLM: `text-embedding-005` via **Vertex AI Embeddings**

* Chosen for **speed**, **accuracy**, and **ease of integration** via Langchain.
* Efficiently converts input text into meaningful **768-dimensional vectors**.
* No manual setup needed when using GCP’s Vertex AI — credentials are mounted inside Docker securely.

### ✅ Data Format: **CSV**

* Simple, lightweight, and universally supported.
* Makes the data easy to inspect and verify outside the application.
* Saves the generated embeddings into `output/embeddings.csv` for debugging and auditability.

### ✅ Vector Database: **Qdrant (NoSQL)**

* Purpose-built for **vector similarity search** — ideal for storing LLM embeddings.
* Open-source and container-friendly.
* Supports **payloads**, which means we can also store the original text alongside the vector for contextual retrieval.

### ✅ Containerization: **Docker + Docker Compose**

* Ensures full reproducibility and isolation.
* Easy to spin up both the ML service and Qdrant with one command.
* Allows environment variables and credentials to be safely injected.

---

## 📁 Project Structure

docker-project/
└── service/
├── app/
│   ├── app.py
│   ├── data_generator.py
│   └── embedding_service.py
├── data/
│   └── generated.csv
├── Dockerfile
├── credentials.json
└── requirements.txt
```

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/arko-14/docker-project-.git
   cd docker-project-
   ```

2. Add your `credentials.json` from Google Cloud to `./service/`

3. Run everything using:

   ```bash
   docker-compose up --build
   ```

4. View logs to confirm embeddings are generated and stored:

   ```bash
   docker logs ml-service-1
   ```

---

## 📦 Output

* ✅ Sample generated embeddings shown in terminal
* ✅ Embeddings saved to `output/embeddings.csv`
* ✅ Vectors + original text upserted into Qdrant at `localhost:6333`

---

## 🔍 Future Enhancements

* Add a REST API to query Qdrant with new text and return most similar entries.
* Add a Streamlit dashboard for visualization.

---

## ✅ Summary

This project showcases:

* End-to-end LLM workflow in Docker
* Usage of a NoSQL vector DB (Qdrant)
* Local-first development and reproducibility
* Clean and modular ML pipeline design

---
