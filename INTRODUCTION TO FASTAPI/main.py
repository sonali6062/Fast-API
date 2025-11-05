from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    """Return a simple greeting."""
    return {"message": "Hello, FastAPI"}
