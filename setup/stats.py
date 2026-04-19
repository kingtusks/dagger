from nba_api.stats.endpoints import playercareerstats

def getSeasonStats(pid: int):
    stats = playercareerstats.PlayerCareerStats(player_id=pid).get_data_frames()
    regStats = stats[0]
    postStats = stats[2]

    regStats = regStats.drop([
        "PLAYER_ID",
        "LEAGUE_ID",
    ], axis=1)

    postStats = postStats.drop([
        "PLAYER_ID",
        "LEAGUE_ID",
    ], axis=1)

    regStats = regStats.rename({"SEASON_ID": "SEASON"}, axis=1)    
    postStats = postStats.rename({"SEASON_ID": "SEASON"}, axis=1)

    regStats = regStats.fillna(0)
    postStats = postStats.fillna(0)

    return regStats, postStats
    
'''
#(TESTING)
bron_id = 2544

stats = formatSeasonStats(bron_id)
reg_season = stats[0]
post_season = stats[1]

reg_season_list = [
    models.SeasonStats(
        player_id   = bron_id,
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
    for row in reg_season.itertuples()
]

post_season_list = [
    models.SeasonStats(
        player_id   = bron_id,
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
    for row in post_season.itertuples()
]

#db.rollback()
#db.add_all(reg_season_list)
#db.add_all(post_season_list)
#db.commit()
#db.close()
'''