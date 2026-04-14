use serde::Serialize;
use axum::Json;

#[derive(Serialize)]
pub struct HomeData {
    pub title: String,
    pub description: String,
}

pub async fn home_data() -> Json<HomeData> {
    Json(HomeData {
        title: "Welcome".to_string(),
        description: "This came from rust!".to_string(), 
    })
}

