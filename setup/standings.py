import models
from nba_api.stats.endpoints import leaguestandings
from season_maker import seasonMaker
from database import engine, sessionDB

models.Base.metadata.create_all(bind=engine)
db = sessionDB()

def getStandings(season: str):
    standings = leaguestandings.LeagueStandings(
        season = season,
        season_type = "Regular Season"
    )

    standings_df = standings.get_data_frames()[0]
    east_df, west_df = standings_df[standings_df["Conference"] == "East"], standings_df[standings_df["Conference"] == "West"]
    return east_df, west_df

def makeModel(df, season, conference):
    player_dict = {}
    conference_enum = models.ConferenceType.east if conference.lower() == "east" else models.ConferenceType.west
    

    return models.Standing(
        season = season,
        conference = conference_enum,
        players = player_dict,
    )

seasons = seasonMaker()

for season in seasons:
    try:
        if db.get(models.Standings, season):
            continue

        standings = getStandings(season)
        east, west = standings[0], standings[1] 

    except Exception as e:
        #db.rollback()
        print(f"failed on season: {season}\n\n{e}")
        break