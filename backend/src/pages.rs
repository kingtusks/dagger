use axum::{Json, extract::{Path, Query, State}};
use chrono::{Datelike, NaiveDate};

use crate::db::AppState;
use crate::structs;
use crate::queries;

pub async fn player_stats(
    State(state): State<AppState>,
    Path(player_name): Path<String>,
) -> Json<Vec<structs::PlayerStats>> {
    let stats = sqlx::query_as(
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
) -> Json<Vec<structs::Countries>> {
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
) -> Json<Vec<structs::Awards>> {
    let awards = sqlx::query_as(
        r#"
        SELECT p.name, a.season, a.award_name
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

    Json(awards)
}

pub async fn birthday(
    State(state): State<AppState>,
    Path(date): Path<String>,
) -> Json<Vec<structs::Birthday>> {

    //we added the 2000 in front cus NaiveDate needs a year (we dont use year anyways)
    let parsed = NaiveDate::parse_from_str(
        &format!("2000-{}", date), 
        "%Y-%m-%d"
    ).unwrap();

    let birthdays = sqlx::query_as(
        r#"
        SELECT p.name, p.birthdate
        FROM players p
        WHERE EXTRACT(MONTH FROM p.birthdate) = $1
            AND EXTRACT(DAY FROM p.birthdate) = $2
        "#,
    )
    .bind(parsed.month() as i32)
    .bind(parsed.day() as i32)
    .fetch_all(&state.pool)
    .await
    .unwrap();

    Json(birthdays)
}

#[allow(non_snake_case)]
pub async fn players_from_country(
    State(state): State<AppState>,
    Path(country): Path<String>,
    Query(query): Query<queries::OrderByQuery>,
) -> Json<Vec<structs::PlayerFromCountry>> {
    let order_by = match query.order_by.as_str() {
        "ast" => "ast",
        "reb" => "reb",
        _ => "pts",
    };

    let sql = format!(
        r#"
        SELECT p.name, p.country, s.pts, s.reb, s.ast
        FROM season_stats s
        JOIN players p ON p.player_id = s.player_id
        WHERE LOWER(p.country) = LOWER($1)
        ORDER BY s.{} DESC
        "#,
        order_by
    );

    let playersFromCountry = sqlx::query_as(&sql)
        .bind(country)
        .fetch_all(&state.pool)
        .await
        .unwrap();

    Json(playersFromCountry)
}

pub async fn general_info(
    State(state): State<AppState>,
    Path(player_name): Path<String>,
) -> Json<Vec<structs::GeneralInfo>> {
    let general_info = sqlx::query_as(
        r#"
        SELECT p.nicknames, p.country, p.school, p.birthdate, p.height, p.weight, p.draft_year,
        p.draft_round, p.draft_pick
        FROM players p
        WHERE LOWER(p.name) = LOWER($1)
        "#,
    )
    .bind(player_name)
    .fetch_all(&state.pool)
    .await
    .unwrap();

    Json(general_info)
}

pub async fn awards_by_season(
    State(state): State<AppState>,
    Path(award_type): Path<String>,
) -> Json<Vec<structs::AwardsBySeason>> {
    let awards = sqlx::query_as(
        r#"
        SELECT a.season, a.award_name
        FROM awards a
        WHERE LOWER(a.award_name) = LOWER($1)
        "#,
    )
    .bind(award_type)
    .fetch_all(&state.pool)
    .await
    .unwrap();

    Json(awards)
}

pub async fn draft_history(
    State(state): State<AppState>,
) -> Json<Vec<structs::DraftHistory>> {
    let draft = sqlx::query_as(
        r#"
        SELECT p.name, p.draft_year, p.draft_round, p.draft_pick
        FROM players p
        "#,
    )
    .fetch_all(&state.pool)
    .await
    .unwrap();

    Json(draft)
}

pub async fn teams(
    State(state): State<AppState>
) -> Json<Vec<>>