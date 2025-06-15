# Gen2Vec


---

# Dockerized ML Service LLM-based Data Generation & Vector embedding utilizing Qdrant


This project shows a containerized machine learning service which:

 *Produces a synthetic data with a **Large Language Model (LLM)**
 *Saves the created data in the form of **CSV file**
 *Embeds the text**
 *Persists the embeddings in a local key-value cache **(Qdrant)**
 *It is all put into a Dockerized pipeline with `docker-compose`.**
.

---

##  So why these choices?

### LLM: `text-embedding-005` by **Vertex AI Embeddings**

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
