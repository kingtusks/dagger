import time
import models
import pandas as pd
from database import engine, sessionDB
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster, playercareerstats

models.Base.metadata.create_all(bind=engine)
db = sessionDB()

season = "2025-26"

all_teams = teams.get_teams()
tid_list = [team["id"] for team in all_teams]

for tid in tid_list:
    try:
        roster = commonteamroster.CommonTeamRoster(
            team_id=tid,
            league_id_nullable="00",
            season=season
        )

        roster_df = roster.get_data_frames()[0]
        player_dict = {}
        
        for row in roster_df.itertuples():
            pid = row.PLAYER_ID
            name = row.PLAYER

            stats = playercareerstats.PlayerCareerStats(player_id=pid)
            stats_df = stats.get_data_frames()[0]
            #print(stats_df)
            current_stats = stats_df[stats_df["SEASON_ID"] == season]
            current_stats = current_stats[current_stats["TEAM_ID"] != 0]

            pts = 0
            reb = 0
            ast = 0
            stock = 0
            gp = 0

            for row in current_stats.itertuples():
                pts += row.PTS
                reb += row.REB
                ast += row.AST
                stock += (row.STL + row.BLK)
                gp += row.GP

            try:
                rlvc = round(((pts + reb + ast + stock) / gp), 2)
            except ZeroDivisionError:
                rlvc = 0.0
    
            player_dict[name] = rlvc
            #print(f"{name}: {points}")
            time.sleep(1)

        sorted_player_dict = {
            k: v 
            for k, v in sorted(player_dict.items(), key=lambda item: item[1], reverse=True)
        }

        team_model = models.Team(
            team_id = tid,
            players = dict(list(sorted_player_dict.items())[:3]),
        )
        
        db.add(team_model)
        db.commit()
        print(f"finished {tid}")
    except Exception as e:
        db.rollback()
        print(f"failed {tid}\n\n{e}")
        break

db.close()