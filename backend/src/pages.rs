use axum::{Json, extract::{Path, State}};
use sqlx::FromRow;
use serde::{Serialize, Deserialize};

use crate::db::AppState;

#[derive(Deserialize, Serialize, FromRow)]
pub struct PlayerStats {
    pub player_name: String,
    pub pts: Option<i32>,
    pub dreb: Option<i32>,
}

pub async fn stats(
    State(state): State<AppState>,
    Path(player_name): Path<String>,
) -> Json<Vec<PlayerStats>> {
    let stats = sqlx::query_as::<_, PlayerStats>(
        r#"
        SELECT p.name AS player_name, s.pts, s.dreb
        FROM season_stats s
        JOIN players p ON p.player_id = s.player_id
        WHERE LOWER(p.name) = LOWER($1)
        "#,
    )
    .bind(player_name)
    .fetch_all(&state.pool)
    .await
    .unwrap();

    Json(stats)
}