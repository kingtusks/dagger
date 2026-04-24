import models
import time
import enum
import pandas as pd
from database import engine, sessionDB
from nba_api.stats.static import players as nba_players
from sqlalchemy.dialects.postgresql import insert
from setup_functions.stats import getSeasonStats
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

def get_current_season() -> str:
    now = datetime.now()
    if now.month >= 10:
        return f"{now.year}-{str(now.year + 1)[-2:]}"
    else:
        return f"{now.year - 1}-{str(now.year)[-2:]}"

def upsert_stats(
    db,
    pid: int,
    season_type: enum.Enum,
    df: pd.DataFrame,
    season: str
) -> None:
    if df.empty:
        return

    for row in df.itertuples():
        stmt = insert(models.SeasonStats).values(
            player_id=pid,
            season=season,
            season_type=season_type,
            team_id=getattr(row, "TEAM_ID", None),
            team_abbr=getattr(row, "TEAM_ABBREVIATION", None),
            player_age=int(row.PLAYER_AGE) if pd.notna(row.PLAYER_AGE) else None,
            gp=int(row.GP),
            gs=int(row.GS),
            minutes=float(row.MIN),
            fgm=int(row.FGM),
            fga=int(row.FGA),
            fg_pct=float(row.FG_PCT) if pd.notna(row.FG_PCT) else None,
            fg3m=int(row.FG3M),
            fg3a=int(row.FG3A),
            fg3_pct=float(row.FG3_PCT) if pd.notna(row.FG3_PCT) else None,
            ftm=int(row.FTM),
            fta=int(row.FTA),
            ft_pct=float(row.FT_PCT) if pd.notna(row.FT_PCT) else None,
            oreb=int(row.OREB),
            dreb=int(row.DREB),
            reb=int(row.REB),
            ast=int(row.AST),
            stl=int(row.STL),
            blk=int(row.BLK),
            tov=int(row.TOV),
            pf=int(row.PF),
            pts=int(row.PTS),
        ).on_conflict_do_update(
            index_elements=["player_id", "season", "team_id", "season_type"],
            set_=dict(
                team_abbr=getattr(row, "TEAM_ABBREVIATION", None),
                player_age=int(row.PLAYER_AGE) if pd.notna(row.PLAYER_AGE) else None,
                gp=int(row.GP),
                gs=int(row.GS),
                minutes=float(row.MIN),
                fgm=int(row.FGM),
                fga=int(row.FGA),
                fg_pct=float(row.FG_PCT) if pd.notna(row.FG_PCT) else None,
                fg3m=int(row.FG3M),
                fg3a=int(row.FG3A),
                fg3_pct=float(row.FG3_PCT) if pd.notna(row.FG3_PCT) else None,
                ftm=int(row.FTM),
                fta=int(row.FTA),
                ft_pct=float(row.FT_PCT) if pd.notna(row.FT_PCT) else None,
                oreb=int(row.OREB),
                dreb=int(row.DREB),
                reb=int(row.REB),
                ast=int(row.AST),
                stl=int(row.STL),
                blk=int(row.BLK),
                tov=int(row.TOV),
                pf=int(row.PF),
                pts=int(row.PTS),
            )
        )
        db.execute(stmt)


def sync_all_players():
    db = sessionDB()
    season = get_current_season()
    active_players = nba_players.get_active_players()

    print(f"[{datetime.now()}] syncing {len(active_players)} players for {season}")

    for player in active_players:
        pid = player["id"]
        name = player["full_name"]

        try:
            stats = getSeasonStats(pid)
            regseason, postseason = stats[0], stats[1]

            reg_rows = regseason[regseason["SEASON"] == season]
            post_rows = postseason[postseason["SEASON"] == season]

            upsert_stats(db, pid, models.SeasonType.regular, reg_rows, season)
            upsert_stats(db, pid, models.SeasonType.playoffs, post_rows, season)

            db.commit()
            print(f"synced {name} ({pid}): {len(reg_rows)} reg rows, {len(post_rows)} post rows")

        except Exception as e:
            db.rollback()
            print(f"error for {name} ({pid}): {e}")

        time.sleep(1)

    db.close()
    print(f"[{datetime.now()}] sync complete")


if __name__ == "__main__":
    sync_all_players()