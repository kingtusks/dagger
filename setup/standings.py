import models
import time
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

def makeModels(df, season, conference):
    conference_enum = models.ConferenceType.east if conference.lower() == "east" else models.ConferenceType.west
    
    standings_list = [
        models.Standing(
            team_id = row.TeamID,
            rank = row.PlayoffRank,
            season = season,
            conference = conference_enum,
        )
        for row in df.itertuples()
    ]

    return standings_list

seasons = seasonMaker()

for idx, season in enumerate(seasons):
    try:
        if db.get(models.Standing, idx + 1):
            continue

        standings = getStandings(season)
        east, west = standings[0], standings[1] 

        east_models = makeModels(east, season, "east")
        west_models = makeModels(west, season, "west")

        db.add_all(east_models)
        db.add_all(west_models)
        db.commit()
        print(f"done with season: {season}")
        time.sleep(1)
    except Exception as e:
        db.rollback()
        print(f"failed on season: {season}\n\n{e}")
        break