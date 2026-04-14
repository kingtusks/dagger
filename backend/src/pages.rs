use axum::{
    extract::Path,
};

pub async fn handler() -> &'static str {
    "allo!"
}

pub async fn greet(Path(name): Path<String>) -> String {
    format!("hello, {}", name)
}