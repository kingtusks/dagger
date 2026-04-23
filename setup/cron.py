import models
import time
import enum
import pandas as pd
from database import engine, sessionDB
from nba_api.stats.static import players
from sqlalchemy import update
from setup_functions.stats import getSeasonStats

models.Base.metadata.create_all(bind=engine)
db = sessionDB()

players = players.get_active_players()

season = "2025-26" #gotta automate season fetching

#gotta figure out how trades work

def updateStats(
    pid: int, 
    season_type: enum.Enum, 
    df: pd.DataFrame, 
    season: str
) -> None:
    db.execute(
        update(models.SeasonStats)
        .where(models.SeasonStats.id == pid)
        .where(models.SeasonStats.season == season)
        .where(models.SeasonStats.season_type == season_type)
        .values(
            player_age = int(df.PLAYER_AGE),
            gp = df["GP"].iloc[0],
            gs = df.GS,
            minutes = df.MIN,
        )
    )



for player in players:
    pid = player["id"]
    stats = getSeasonStats(pid)
    regseason, postseason = stats[0], stats[1]
    
    regseason = regseason[regseason["SEASON"] == season]
    postseason = postseason[postseason["SEASON"] == season]
    
    #print(regseason)
    break
    
    try:
        #updateStats(pid, models.SeasonType.regular, regseason)
        #updateStats(pid, models.SeasonType.playoffs, postseason)
        print(f"updated for {player["full_name"]}: {pid}")
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"stats error: {e}")
    time.sleep(1)


