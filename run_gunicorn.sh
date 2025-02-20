#!/usr/bin/env bash

# Make migrations in DB
# echo "Start mirgration"
# alembic upgrade head
# echo "Stop mirgration"

# Start up server
gunicorn -w ${NUM_WORKERS} -k uvicorn.workers.UvicornWorker -b ${BIND_HOST}:${PORT} --timeout 180 --access-logfile - --error-logfile - wsgi:app