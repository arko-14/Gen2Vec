import os
from flask import Flask, request, jsonify
from data_generator import generate_data
from embedding_service import embed_and_store

app = Flask(__name__)
DATA_CSV = "/app/data/generated.csv"

@app.route('/generate', methods=['POST'])
def generate():
    n = int(request.args.get('n', 100))
    try:
        df = generate_data(DATA_CSV, n)
        return jsonify(status="success", rows=len(df))
    except Exception as e:
        return jsonify(status="error", detail=str(e)), 500

@app.route('/embed', methods=['POST'])
def embed():
    try:
        count = embed_and_store(DATA_CSV)
        return jsonify(status="success", points_indexed=count)
    except Exception as e:
        return jsonify(status="error", detail=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)