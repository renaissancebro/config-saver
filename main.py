from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Config(BaseModel):
    ticker: str
    threshold: float


@app.post("/save")
def save_config(config: Config):
    print(f"Received: {config}")
    return {"message": "Config saved!", "config": config}
