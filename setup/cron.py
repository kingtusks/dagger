import time
import models
import pandas as pd
from database import engine, sessionDB
from nba_api.stats.static import players
from datetime import datetime

from setup_functions.agent import getExtraPlayerInfo
from setup_functions.player import getPlayerInfo, to_CM
from setup_functions.award import getAwards
from setup_functions.stats import getSeasonStats

active_players = players.get_active_players()

models.Base.metadata.create_all(bind=engine)
db = sessionDB()

year = "2025-26"

for player in active_players:
    
