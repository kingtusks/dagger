#!/bin/bash

set -e

export $(grep -v '^#' .env | xargs)

DB_URL=${POSTGRES_URL}

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${TIMESTAMP}.sql"

pg_dump "$DB_URL" > "$BACKUP_FILE"

echo "backup saved to $BACKUP_FILE"