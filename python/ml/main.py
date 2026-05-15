from fastapi import FastAPI
from models.season import predictSeason, SeasonData

app = FastAPI()

#need rust to give me a list of structured data to pass in predictSeason
@app.get("/ml/predict/season/{player_name}")
async def predictSeasonStats(player_name: str, season_data: dict[str, SeasonData]):
    return predictSeason(player_name, season_data)