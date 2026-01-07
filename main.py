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

@app.get("/api/scores/easy")
async def get_easy_scores():
    easy_scores = [score for score in scores_database if score.diff == "Easy"]
    sorted_scores_easy = sorted(easy_scores, key=lambda x: float(x.time))
    return sorted_scores_easy

@app.get("/api/scores/medium")
async def get_medium_scores():  
    medium_scores = [score for score in scores_database if score.diff == "Medium"]
    sorted_scores_medium = sorted(medium_scores, key=lambda x: float(x.time))
    return sorted_scores_medium

@app.get("/api/scores/hard")
async def get_hard_scores():
    hard_scores = [score for score in scores_database if score.diff == "Hard"]
    sorted_scores_hard = sorted(hard_scores, key=lambda x: float(x.time))
    return sorted_scores_hard