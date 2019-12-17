FROM tiangolo/uvicorn-gunicorn:python3.7
LABEL maintainer="Fanch <francois.valadier@openvalue.fr>"

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY ./app /app