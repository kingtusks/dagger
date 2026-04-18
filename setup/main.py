from database import engine, sessionDB
from nba_api.stats.static import players
from datetime import datetime
from agent import getExtraPlayerInfo
import models

players= players.get_players()

models.Base.metadata.create_all(bind=engine)
db = sessionDB()



    