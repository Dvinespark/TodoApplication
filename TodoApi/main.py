from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "Fast api is running"}