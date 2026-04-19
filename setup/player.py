from nba_api.stats.endpoints import commonplayerinfo

def to_CM(height: str):
    try:
        height = height.split("-")
        return round(int(height[0]) * 30.48 + int(height[1]) * 2.54)
    except:
        return None

def getPlayerInfo(pid: int):
    info_df = commonplayerinfo.CommonPlayerInfo(player_id=pid).get_data_frames()[0] 

    needed_columns = [
        "DISPLAY_FIRST_LAST", 
        "BIRTHDATE", 
        "COUNTRY", 
        "HEIGHT", 
        "WEIGHT", 
        "DRAFT_YEAR", 
        "DRAFT_ROUND", 
        "DRAFT_NUMBER"
    ]

    #nicknames and school i need to use an agent for

    info_df = info_df[needed_columns]
    info_df = info_df.rename({"DISPLAY_FIRST_LAST": "NAME"}, axis=1)

    for col in ["DRAFT_YEAR", "DRAFT_ROUND", "DRAFT_NUMBER", "HEIGHT", "WEIGHT"]:
        info_df[col] = info_df[col].apply(lambda x: int(x) if str(x).isdigit() else None)

    return info_df

'''
#(TESTING)
bron_id = 2544

info_df = getPlayer(bron_id)
player_name = info_df["NAME"].iloc[0]

extra_info = None
while not extra_info:
    extra_info = getExtraPlayerInfo(player_name)

print(extra_info)

pinfo = models.Player(
    player_id = bron_id, #dont hardcode this in prod
    name = info_df["NAME"].iloc[0],
    nicknames = extra_info['nicknames'],
    country = info_df["COUNTRY"].iloc[0],
    school = extra_info['college'],
    birthdate = datetime.fromisoformat(info_df["BIRTHDATE"].iloc[0]).date(),
    height = to_CM(info_df["HEIGHT"].iloc[0]),
    weight = int(info_df["WEIGHT"].iloc[0]),
    draft_year = int(info_df["DRAFT_YEAR"].iloc[0]),
    draft_round = int(info_df["DRAFT_ROUND"].iloc[0]),
    draft_pick = int(info_df["DRAFT_NUMBER"].iloc[0]),
)

#db.rollback()
#db.add(pinfo)
#db.commit()
#db.close()
'''