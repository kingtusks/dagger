import os
import sys
import time
from nba_api.stats.endpoints import leagueleaders
from nba_api.stats.endpoints import leaguestandings
from populator_helpers.season_maker import seasonMaker

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

import models
from database import engine, sessionDB

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
            record = row.Record,
            season = season,
            conference = conference_enum,
        )
        for row in df.itertuples()
    ]

    return standings_list

def getStatLeaders(season: str):
    start_year = int(season.split("-")[0])
    categories = ["PTS", "REB", "AST"] if start_year < 1973 else ["PTS", "REB", "AST", "STL", "BLK"]
    leader_dict = {}

    for category in categories:
        leaders = leagueleaders.LeagueLeaders(
            league_id = "00",
            season = season,
            per_mode48 = "PerGame", #!!!
            stat_category_abbreviation = category,
            season_type_all_star = "Regular Season",
            scope = "S",
        )

        leader_df = leaders.get_data_frames()[0].iloc[0]
        leader_dict[category] = {leader_df["PLAYER"]: float(leader_df[category])}
        time.sleep(1)
        #print(f"done with {season}: {category}")
    return leader_dict

def populateSeasonInfo():
    models.Base.metadata.create_all(bind=engine)
    db = sessionDB()
    season_list = seasonMaker()

    for idx, season in enumerate(season_list):
        try:
            if db.get(models.Leaders, season) and db.get(models.Standing, idx + 1):
                continue

            standings = getStandings(season)
            east, west = standings[0], standings[1]

            east_models = makeModels(east, season, "east")
            west_models = makeModels(west, season, "west")

            leaders = getStatLeaders(season)
            start_year = int(season.split("-")[0])

            if start_year < 1973:
                leader_model = models.Leaders(
                    season = season,
                    pts = leaders["PTS"],
                    reb = leaders["REB"],
                    ast = leaders["AST"],
                )
            else:
                leader_model = models.Leaders(
                    season = season,
                    pts = leaders["PTS"],
                    reb = leaders["REB"],
                    ast = leaders["AST"],
                    stl = leaders["STL"],
                    blk = leaders["BLK"],
                )
            db.add(leader_model)
            db.add_all(east_models)
            db.add_all(west_models)
            db.commit()
            print(f"done with season: {season}")
            time.sleep(1)
        except Exception as e:
            db.rollback()
            print(f"failed at season: {season}\n\n{e}")
            break