use serde::{Serialize, Deserialize};
use serde_json::Value;
use sqlx::FromRow;
use chrono::NaiveDate;

#[derive(Deserialize, Serialize, FromRow)]
pub struct PlayerStats {
    pub name: String,
    pub season: Option<String>,
    pub team_abbr: Option<String>,
    pub season_type: String,
    pub player_age: Option<i32>,
    pub gp: Option<i32>,
    pub gs: Option<i32>,
    pub minutes: Option<i32>,
    pub fgm: Option<i32>,
    pub fga: Option<i32>,
    pub fg_pct: Option<f64>,
    pub fg3m: Option<i32>,
    pub fg3a: Option<i32>,
    pub fg3_pct: Option<f64>,
    pub ftm: Option<i32>,
    pub fta: Option<i32>,
    pub ft_pct: Option<f64>,
    pub oreb: Option<i32>,
    pub dreb: Option<i32>,
    pub reb: Option<i32>,
    pub ast: Option<i32>,
    pub stl: Option<i32>,
    pub blk: Option<i32>,
    pub tov: Option<i32>,
    pub pf: Option<i32>,
    pub pts: Option<i32>,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct Countries {
    pub name: String,
    pub country: String,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct Awards {
    pub name: String,
    pub award_name: String,
    pub season: String,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct Birthday {
    pub name: String,
    pub birthdate: Option<NaiveDate>,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct PlayerFromCountry {
    pub name: String,
    pub country: String,
    pub pts: i32,
    pub reb: i32,
    pub ast: i32,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct GeneralInfo {
    pub nicknames: Value,
    pub country: String,
    pub school: String,
    pub birthdate: Option<NaiveDate>,
    pub height: i32,
    pub weight: i32,
    pub draft_year: i32,
    pub draft_round: i32,
    pub draft_pick: i32,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct AwardsBySeason {
    pub season: String,
    pub award_name: String,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct DraftHistory {
    pub name: String,
    pub draft_year: i32,
    pub draft_round: i32,
    pub draft_pick: i32,
    //pub school: String,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct TeamInfo {
    pub team_id: i32,
    //add season
    pub abbreviation: String,
    pub name: String,
    pub state: String,
    pub year_founded: i32,
    pub players: Value,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct LeagueLeaders {
    pub season: String,
    pub pts: Value,
    pub reb: Value,
    pub ast: Value,
    pub stl: Option<Value>,
    pub blk: Option<Value>,
}

#[derive(Deserialize, Serialize, FromRow)]
pub struct Standings {
    pub team_id: i32,
    pub name: String,
    pub abbreviation: String,
    pub rank: i32, 
    pub record: String,
    pub season: String,
    pub conference: String,
}

//everything under here is gonna be for the prediction stuff

#[derive(Deserialize, Serialize, FromRow)]
pub struct SeasonData {
    player_age: i32,
    //season: String,
    team_abbr: String,
    //teammates: Vec<String>,
    //position: String,
    minutes: i32,
    gp: i32,
    gs: i32,
    fg_pct: f64,
    ft_pct: f64,
    pts: i32,
    oreb: i32,
    dreb: i32,
    ast: i32,
    stl: i32,
    blk: i32,
}