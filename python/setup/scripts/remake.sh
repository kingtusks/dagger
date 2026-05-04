#!/bin/bash

su -i -u postgres
psql

SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'dagger' and pid <> pg_backend_pid();

DROP database dagger;
CREATE database dagger;