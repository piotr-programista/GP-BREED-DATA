from fastapi import FastAPI

app = FastAPI(title="GP BREED DATA API")

@app.get("/health")
def health():
    return {"status": "ok"}