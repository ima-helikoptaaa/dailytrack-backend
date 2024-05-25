from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World!"}
