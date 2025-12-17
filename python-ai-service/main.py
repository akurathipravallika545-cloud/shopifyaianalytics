from fastapi import FastAPI
app = FastAPI()

@app.post("/analyze")
def analyze(payload: dict):
    return {
        "answer": "You sell around 10 units per day. Reorder 70 units.",
        "confidence": "medium"
    }
