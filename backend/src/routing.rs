use axum::{Router, routing::get};
use tower_http::cors::CorsLayer;

use crate::pages;
use crate::db;

pub async fn app() -> Router {
    let state = db::pool().await;
    Router::new()
        .route("/api/stats/{player_name}", get(pages::stats))
        .with_state(state)
        .layer(CorsLayer::permissive())
}