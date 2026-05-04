#!/bin/bash

cargo install sqlx-cli --no-default-features --features postgres
cargo sqlx prepare