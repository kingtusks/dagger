import models
import time
import pandas as pd
from database import engine, sessionDB
from nba_api.stats.static import players
from datetime import datetime

from setup_functions.agent import getExtraPlayerInfo
from setup_functions.player import getPlayerInfo, to_CM
from setup_functions.award import getAwards
from setup_functions.stats import getSeasonStats

players= players.get_players()

models.Base.metadata.create_all(bind=engine)
db = sessionDB()

try:
    with open("fails.txt", "r") as f:
        failed_ids = {int(line.split(": ")[1]) for line in f if line.strip()}
except FileNotFoundError:
    failed_ids = set()

for player in players:
    try:
        pid = player["id"]

        if pid in failed_ids:
            continue

        if db.get(models.Player, pid):
            continue
        
        info_df = getPlayerInfo(pid)
        pname = info_df["NAME"].iloc[0]

        extra_info = None
        while not extra_info:
            extra_info = getExtraPlayerInfo(pname)

        pinfo = models.Player(
            player_id = pid,
            name = pname,
            nicknames = extra_info['nicknames'],
            country = info_df["COUNTRY"].iloc[0],
            school = extra_info['college'],
            birthdate = datetime.fromisoformat(info_df["BIRTHDATE"].iloc[0]).date(),
            height = to_CM(info_df["HEIGHT"].iloc[0]) if info_df["HEIGHT"].iloc[0] else 0,
            weight = int(info_df["WEIGHT"].iloc[0]) if info_df["WEIGHT"].iloc[0] else 0,
            draft_year = int(info_df["DRAFT_YEAR"].iloc[0]) if info_df["DRAFT_YEAR"].iloc[0] else 0,
            draft_round = int(info_df["DRAFT_ROUND"].iloc[0]) if info_df["DRAFT_ROUND"].iloc[0] else 0,
            draft_pick = int(info_df["DRAFT_NUMBER"].iloc[0]) if info_df["DRAFT_NUMBER"].iloc[0] else 0,
        )


        stats = getSeasonStats(pid)
        regseason = stats[0]
        postseason = stats[1]

        try:
            reg_season_list = [
                models.SeasonStats(
                    player_id   = pid,
                    season      = row.SEASON,
                    team_id     = row.TEAM_ID,
                    team_abbr   = row.TEAM_ABBREVIATION,
                    season_type = models.SeasonType.regular,
                    player_age  = int(row.PLAYER_AGE),
                    gp          = row.GP,
                    gs          = row.GS,
                    minutes     = row.MIN,
                    fgm         = row.FGM,
                    fga         = row.FGA,
                    fg_pct      = row.FG_PCT,
                    fg3m        = row.FG3M,
                    fg3a        = row.FG3A,
                    fg3_pct     = row.FG3_PCT,
                    ftm         = row.FTM,
                    fta         = row.FTA,
                    ft_pct      = row.FT_PCT,
                    oreb        = row.OREB,
                    dreb        = row.DREB,
                    reb         = row.REB,
                    ast         = row.AST,
                    stl         = row.STL,
                    blk         = row.BLK,
                    tov         = row.TOV,
                    pf          = row.PF,
                    pts         = row.PTS,
                )
                for row in regseason.itertuples()
            ]

            post_season_list = [
                models.SeasonStats(
                    player_id   = pid,
                    season      = row.SEASON,
                    team_id     = row.TEAM_ID,
                    team_abbr   = row.TEAM_ABBREVIATION,
                    season_type = models.SeasonType.playoffs,
                    player_age  = int(row.PLAYER_AGE),
                    gp          = row.GP,
                    gs          = row.GS,
                    minutes     = row.MIN,
                    fgm         = row.FGM,
                    fga         = row.FGA,
                    fg_pct      = row.FG_PCT,
                    fg3m        = row.FG3M,
                    fg3a        = row.FG3A,
                    fg3_pct     = row.FG3_PCT,
                    ftm         = row.FTM,
                    fta         = row.FTA,
                    ft_pct      = row.FT_PCT,
                    oreb        = row.OREB,
                    dreb        = row.DREB,
                    reb         = row.REB,
                    ast         = row.AST,
                    stl         = row.STL,
                    blk         = row.BLK,
                    tov         = row.TOV,
                    pf          = row.PF,
                    pts         = row.PTS,
                )
                for row in postseason.itertuples()
            ]
        except Exception as e:
            print(f"stats error: {e}")

        awards = getAwards(pid)

        award_list = [
            models.Award(
                player_id = pid, #dont hardcode this in prod
                season = award.SEASON,
                award_name = award.DESCRIPTION
            )
            for award in awards.itertuples()
        ]

        db.add(pinfo)
        db.add_all(reg_season_list)
        db.add_all(post_season_list)
        db.add_all(award_list)
        db.commit()
        print(f"finished {player["full_name"]}: {player["id"]}")
        time.sleep(1)
    except KeyError as e:
        print(f"failed on {player["full_name"]}: {player["id"]} \n\n{e}")
        with open("fails.txt", "a") as f:
            f.write(f"{player["full_name"]}: {player["id"]}\n")
        #break
    except Exception as e:
        db.rollback()
        print(f"failed on {player["full_name"]}: {player["id"]} \n\n{e}")
        break

db.close()    