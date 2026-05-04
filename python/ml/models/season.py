import numpy as np
import pandas as pd
from pydantic import BaseModel

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

def predictSeason(seasons: list[SeasonData], player_name: str):
    #convert list of season datas to dataframe
    df = pd.DataFrame([season.model_dump() for season in seasons])

    return {"a": "stub"}