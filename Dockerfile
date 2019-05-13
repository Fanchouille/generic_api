FROM tiangolo/uvicorn-gunicorn:python3.6

LABEL maintainer="Fanch <francois.valadier@openvalue.fr>"

RUN pip install fastapi scikit-learn python-multipart joblib

COPY ./app /app