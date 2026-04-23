import models
import time
import pandas as pd
from database import engine, sessionDB
from nba_api.stats.static import players
from sqlalchemy import update
from setup_functions.stats import getSeasonStats

models.Base.metadata.create_all(bind=engine)
db = sessionDB()

players = players.get_active_players()

def updateStats(pid, season_type, df):
    db.execute(
        update(models.SeasonStats)
        .where(
            models.SeasonStats.id == pid,
            models.SeasonStats.season == 
            models.SeasonStats.season_type == season_type,
        )
        .values(
            nicknames="The King",
            school="Ohio State"
        )
    )

for player in players:
    pid = player["id"]
    stats = getSeasonStats(pid)
    regseason, postseason = stats[0], stats[1]
    try:
        updateStats(pid, models.SeasonType.regular, regseason)
        updateStats(pid, models.SeasonType.playoffs, postseason)
        print(f"updated for {player["full_name"]}: {pid}")
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"stats error: {e}")
    time.sleep(1)


