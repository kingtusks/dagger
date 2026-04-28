import time
import models
from database import engine, sessionDB
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
from setup_functions.stats import getSeasonStats

