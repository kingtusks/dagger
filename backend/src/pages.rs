use serde::{Serialize, Deserialize};
use axum::{Json, extract::Path};
use sqlx::FromRow;

#[derive(Deserialize, Serialize, FromRow)]
pub struct PlayerStats {
    pub player_name: String,
    pub pts: i32,
    pub dreb: i32,
}

pub async fn stats(Path(player_name): Path<String>) -> Json<PlayerStats> {

    Json(PlayerStats {
        player_name: player_name,
        pts: 11,
        dreb: 7,
    })
}
