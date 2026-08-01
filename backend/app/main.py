from fastapi import FastAPI

app = FastAPI(
    title="AstraQuant API",
    description="AI-powered investment intelligence platform",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "project": "AstraQuant",
        "status": "running"
    }