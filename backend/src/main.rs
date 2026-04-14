use axum::{Router, routing::get};
use tower_http::cors::CorsLayer;

mod pages;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/api/home", get(pages::home_data))
        .layer(CorsLayer::permissive());

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();

    println!("listening on http://localhost:3000");
    axum::serve(listener, app).await.unwrap();
}