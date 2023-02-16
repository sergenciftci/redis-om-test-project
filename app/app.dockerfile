# FROM python:3.11.1

# RUN apt-get update && apt-get install -yq python3 python3-pip python3-dev curl libsnmp-dev gcc wget tar libperl-dev default-libmysqlclient-dev build-essential iputils-ping && apt-get autoremove -y && apt-get clean

# WORKDIR /app/

# # Install Poetry
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
# ENV PATH="/root/.local/bin:$PATH"
# RUN poetry config virtualenvs.create false

# # Copy poetry.lock* in case it doesn't exist in the repo
# COPY ./pyproject.toml ./poetry.lock* /app/

# # Allow installing dev dependencie<s to run tests
# ARG INSTALL_DEV=false
# RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# ENV PYTHONPATH=/app

# EXPOSE 80


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
# python setup.py build_ext --inplace
WORKDIR /app
# RUN poetry add /gevent_snmp
