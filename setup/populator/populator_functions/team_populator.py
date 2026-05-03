import os
import sys
import time
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster, playercareerstats

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

import models
from database import engine, sessionDB

def populateTeams(season: str):
    models.Base.metadata.create_all(bind=engine)
    db = sessionDB()
    all_teams = teams.get_teams()

    for team_dict in all_teams:
        tid = team_dict["id"]
        team_abbr = team_dict["abbreviation"]
        team_name = team_dict["full_name"]
        team_state = team_dict["state"]
        year_founded = team_dict["year_founded"]

        try:
            if db.get(models.Team, tid):
                continue

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

                current_stats = stats_df[stats_df["SEASON_ID"] == season]
                current_stats = current_stats[current_stats["TEAM_ID"] != 0]

                pts = reb = ast = stock = gp = 0
                for stat_row in current_stats.itertuples():
                    pts += stat_row.PTS
                    reb += stat_row.REB
                    ast += stat_row.AST
                    stock += (stat_row.STL + stat_row.BLK)
                    gp += stat_row.GP

                try:
                    rlvc = round(((pts + reb + ast + stock) / gp), 2)
                except ZeroDivisionError:
                    rlvc = 0.0

                player_dict[name] = rlvc
                time.sleep(1)

            sorted_player_dict = {
                k: v
                for k, v in sorted(player_dict.items(), key=lambda item: item[1], reverse=True)
            }

            team_model = models.Team(
                team_id=tid,
                abbreviation=team_abbr,
                name=team_name,
                state=team_state,
                year_founded=year_founded,
                players=sorted_player_dict,
            )

            db.add(team_model)
            db.commit()
            print(f"finished {tid}")

        except Exception as e:
            db.rollback()
            print(f"failed {tid}\n\n{e}")
            break

    db.close()