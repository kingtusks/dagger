from fastapi import FastAPI
from models.season import predictSeason, SeasonData

app = FastAPI()

@app.post("/ml/predict/season/{player_name}")
async def predictSeasonStats(player_name: str, season_data: list[SeasonData]):
    return predictSeason(player_name, season_data)