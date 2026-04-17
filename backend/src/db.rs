use sqlx::PgPool;

#[derive(Clone)]
pub struct AppState {
    pool: PgPool,
}

pub async fn pool() -> AppState {
    let pool = PgPool::connect("/").await.unwrap();
    AppState {pool}
}