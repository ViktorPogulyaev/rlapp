FROM python:3.12.5-slim-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /deploy/app

RUN apt-get -y update && \
    apt-get install -y gcc libpq-dev python3-dev build-essential && \
    mkdir -p /deploy/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    chmod +x /deploy/app/run_gunicorn.sh

CMD ./run_gunicorn.sh