from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScoreRecu(BaseModel):
    name: str
    time: int
    attempts: int
    diff: str

scores_database = []

@app.post("/api/save-score")
async def save_score(data: ScoreRecu):
    scores_database.append(data)
    print(f"Nouveau score reçu ! Joueur: {data.name}, Temps: {data.time}")

    return {
        "status": "success", 
        "message": f"Bravo {data.name}, ton score est enregistré !",
        "total_scores": len(scores_database)
    }

@app.get("/api/scores")
async def get_all_scores():
    return scores_database