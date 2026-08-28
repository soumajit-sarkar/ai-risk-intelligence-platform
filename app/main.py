from fastapi import FastAPI

app = FastAPI(title="RGS")


@app.get("/health")
def health_check():
    return {"status": "ok"}