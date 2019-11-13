FROM tiangolo/uvicorn-gunicorn:python3.7
LABEL maintainer="Fanch <francois.valadier@openvalue.fr>"

RUN pip install starlette==0.11.1 fastapi==0.40 scikit-learn python-multipart joblib

COPY ./app /app