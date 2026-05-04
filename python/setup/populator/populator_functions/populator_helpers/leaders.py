import time
import models
from database import sessionDB, engine
from nba_api.stats.endpoints import leagueleaders
from season_maker import seasonMaker

#season

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

models.Base.metadata.create_all(bind=engine)
db = sessionDB()

seasons = seasonMaker()

for season in seasons:
    try:
        if db.get(models.Leaders, season):
            continue
        
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
        db.commit()
        print(f"finished {season}")
    except Exception as e:
        db.rollback()
        print(f"error for {season}:\n\n{e}")
        break
