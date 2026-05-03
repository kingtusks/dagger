from nba_api.stats.endpoints import playerawards

def getAwards(pid: int):
    awards_df = playerawards.PlayerAwards(player_id=pid).get_data_frames()[0]

    acronym_hmap = {
        "All-Defensive Team": "DEF",''
        "All-NBA": "NBA",
        "All-Rookie Team": "ROOK",
        "NBA All-Star": "AS",
        "NBA All-Star Most Valuable Player": "ASMVP",
        "NBA Champion": "CHAMP",
        "NBA Cup All-Tournament Team": "CUP",
        "NBA Cup Most Valuable Player": "CUPMVP",
        "NBA Finals Most Valuable Player": "FMVP",
        "NBA Most Valuable Player": "MVP",
        "NBA Player of the Month": "POTM",
        "NBA Player of the Week": "POTW",
        "NBA Rookie of the Month": "ROTM",
        "NBA Rookie of the Year": "ROTY",
    }

    all_nba_set = {"DEF", "NBA", "ROOK", "CUP"}

    awards_df = awards_df[awards_df["DESCRIPTION"].isin(acronym_hmap)]
    awards_df = awards_df.drop([
        "FIRST_NAME", 
        "LAST_NAME", 
        "CONFERENCE", 
        "TYPE", 
        "SUBTYPE1", 
        "SUBTYPE2", 
        "SUBTYPE3",
        "MONTH",
        "WEEK",
        "PERSON_ID",
        "TEAM"
    ], axis=1)

    awards_df["ALL_NBA_TEAM_NUMBER"] = awards_df["ALL_NBA_TEAM_NUMBER"].fillna(0)
    awards_df = awards_df.replace(r'^\s*$', 0, regex=True) 
    #^ gets rid of empty strings

    awards_df["DESCRIPTION"] = awards_df["DESCRIPTION"].map(acronym_hmap)
    awards_df["DESCRIPTION"] = awards_df.apply(
        lambda r: f"{r['DESCRIPTION']}{r['ALL_NBA_TEAM_NUMBER']}" 
        if r['DESCRIPTION'] in all_nba_set else r['DESCRIPTION'], 
        axis=1
    )

    return awards_df.drop(["ALL_NBA_TEAM_NUMBER"], axis=1)

'''
#(TESTING)
bron_id = 2544

awards = getAwards(bron_id)

award_list = [
    models.Award(
        player_id = bron_id, #dont hardcode this in prod
        season = award.SEASON,
        award_name = award.DESCRIPTION
    )
    for award in awards.itertuples()
]

#db.rollback()
#db.add_all(award_list)
#db.commit()
#db.close()
'''