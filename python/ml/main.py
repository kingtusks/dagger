from fastapi import FastAPI
from pydantic import BaseModel
from models import season

app = FastAPI()

#class GameData(BaseModel):

class SeasonData(BaseModel):
    age: int
    season: str
    team: str
    teammates: list[str]
    position: str
    minutes: int
    usage_pct: float
    gp: int
    gs: int
    fg_pct: float
    ts_pct: float
    pts: int
    oreb: int
    dreb: int
    ast: int
    stl: int
    blk: int

#@app.get("/ml/predict/game")
#async def predict_game_stats(game_data: GameData):
#    return {"stub": "stub"}

@app.get("/ml/predict/season/{player_name}")
async def predict_season_stats(season_data: SeasonData, player_name: str):
    
    return {"stub": "stub"}