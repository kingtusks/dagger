use axum::{
    Router, 
    routing::{get}
};

mod pages;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(pages::handler))
        .route("/greet/{name}", get(pages::greet));

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();

    println!("listening on http://localhost:3000");
    axum::serve(listener, app).await.unwrap();
}
