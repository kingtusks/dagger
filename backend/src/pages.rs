use axum::{Json, extract::{Path, State}};
use sqlx::FromRow;
use serde::{Serialize, Deserialize};

use crate::db::AppState;

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
    pub award: String,
    pub year: String,
}

//fuck structs

pub async fn player_stats(
    State(state): State<AppState>,
    Path(player_name): Path<String>,
) -> Json<Vec<PlayerStats>> {
    let stats = sqlx::query_as::<_, PlayerStats>(
        r#"
        SELECT p.name, s.season, s.team_abbr, s.season_type::TEXT AS season_type,
            s.player_age, s.gp, s.gs, s.minutes, s.fgm, s.fga, s.fg_pct,
            s.fg3m, s.fg3a, s.fg3_pct, s.ftm, s.fta, s.ft_pct,
            s.oreb, s.dreb, s.reb, s.ast, s.stl, s.blk, s.tov, s.pf, s.pts
        FROM season_stats s
        JOIN players p ON p.player_id = s.player_id
        WHERE LOWER(p.name) = LOWER($1)
        ORDER BY s.season ASC
        "#,
    )
    .bind(player_name)
    .fetch_all(&state.pool)
    .await
    .unwrap();

    Json(stats)
}

pub async fn countries( //(change this later i just want an endpoint for now)
    State(state): State<AppState>,
) -> Json<Vec<Countries>> {
    let countries = sqlx::query_as(
        r#"
        SELECT p.name, p.country
        FROM players p
        "#,
    )
    .fetch_all(&state.pool)
    .await
    .unwrap();

    Json(countries)
}

pub async fn awards(
    State(state): State<AppState>,
    Path(player_name): Path<String>,
) -> Json<Vec<Awards>> {
    let award = sqlx::query_as(
        r#"
        SELECT a.season, a.award_name
        FROM awards a
        JOIN players p ON p.player_id = a.player_id
        WHERE LOWER(p.name) = LOWER($1)
        ORDER BY a.season ASC
        "#,
    )
    .bind(player_name)
    .fetch_all(&state.pool)
    .await
    .unwrap();
    Json(award)
}