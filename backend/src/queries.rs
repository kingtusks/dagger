use serde::Deserialize;

fn default_order_by() -> String {
    "pts".to_string()
}

#[derive(Deserialize)]
pub struct OrderByQuery {
    #[serde(default = "default_order_by")]
    pub order_by: String,
}