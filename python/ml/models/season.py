import numpy as np
import pandas as pd
from pydantic import BaseModel

class SeasonData(BaseModel):
    player_age: int
    season: str
    team_abbr: str
    #teammates: list[str]
    #position: str
    minutes: int
    gp: int
    gs: int
    fg_pct: float
    ft_pct: float
    pts: int
    oreb: int
    dreb: int
    ast: int
    stl: int
    blk: int

def predictSeason(player_name: str, ):
    #convert list of season datas to dataframe

    return {"a": "stub"}