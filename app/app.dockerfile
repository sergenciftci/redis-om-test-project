FROM python:3.11.1

RUN apt-get update && \
    apt-get install -yq python3 python3-pip python3-dev curl libsnmp-dev gcc wget tar libperl-dev build-essential iputils-ping supervisor nano ca-certificates && \
    apt-get autoremove -y && apt-get clean

WORKDIR /
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false

COPY . /app

RUN rm /app/app.dockerfile
WORKDIR /app

RUN bash -c "poetry install --no-root --no-dev"
ENV PYTHONPATH=/app