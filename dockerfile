FROM python:3.10-slim-buster

RUN apt update --no-install-recommends -y

ARG SETUP

ENV SETUP=${SETUP} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.13

RUN pip install "poetry==$POETRY_VERSION"

RUN mkdir /app
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install  --no-dev --no-interaction --no-ansi

COPY . /app

CMD ["python3", "birthy/main.py"]