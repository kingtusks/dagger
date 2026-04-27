use axum::{Router, routing::get};
use tower_http::cors::CorsLayer;

use crate::pages;
use crate::db;

pub async fn app() -> Router {
    let state = db::create_pool().await;
    Router::new()
        .route("/api/stats/{player_name}", get(pages::player_stats))
        .route("/api/general_info/{player_name}", get(pages::general_info))
        .route("/api/awards/{player_name}", get(pages::awards))
        .route("/api/countries", get(pages::countries))
        .route("/api/countries/{country}", get(pages::players_from_country))
        .route("/api/birthdays/{date}", get(pages::birthday))
        .route("/api/awards_by_season/{award_type)", get(pages::awards_by_season))
        .route("/api/draft_history", get(pages::draft_history))
        .with_state(state)
        .layer(CorsLayer::permissive())
}