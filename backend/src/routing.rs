use axum::{Router, routing::get};
use tower_http::cors::CorsLayer;

use crate::pages;
use crate::db;

pub async fn app() -> Router {
    let state = db::create_pool().await;
    Router::new()
        .route("/api/stats/{player_name}", get(pages::player_stats))
        .route("/api/countries", get(pages::countries))
        .with_state(state)
        .layer(CorsLayer::permissive())
}