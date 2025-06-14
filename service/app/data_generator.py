
import os
import json
import pandas as pd
from langchain_google_vertexai import VertexAI  # Correct import

def clean_json_response(response: str) -> str:
    """
    Cleans triple-backtick and other formatting around JSON to ensure it's parseable.
    """
    response = response.strip()
    if response.startswith("```json"):
        response = response[7:]  # Remove ```json
    elif response.startswith("```"):
        response = response[3:]  # Remove ```
    if response.endswith("```"):
        response = response[:-3]  # Remove ending ```
    return response.strip()

def generate_data(output_csv: str, n: int = 100):
    llm = VertexAI(
        model_name="gemini-2.0-flash-001",
        temperature=0.7,
        project="gen-lang-client-0378774532"  # Hardcoded project ID
    )
    llm.model_rebuild()  # Needed for Pydantic v2

    rows = []
    for i in range(n):
        prompt = (
            f"Return ONLY a JSON object in this format: "
            f'{{"id": {i+1}, "text": "Sample text for ID {i+1}"}} '
            "Do not include any explanation or prefix. Just return the JSON object."
        )
        result = llm(prompt)
        print("Prompt Result:", result)
        print("⏳ Using project:", os.getenv("PROJECT_ID"))

        try:
            clean_result = clean_json_response(result)
            record = json.loads(clean_result)
            rows.append(record)
        except Exception as e:
            print(f"⚠️ JSON parse failed for record {i+1}: {e}")
            continue

    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)
    return df
