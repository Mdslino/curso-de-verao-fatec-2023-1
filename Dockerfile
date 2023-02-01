FROM python:3.10.7-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y curl make && apt clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-cache

COPY . .

EXPOSE 8000