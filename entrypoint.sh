#!/usr/bin/env bash
eval "$(conda shell.bash hook)"
conda activate ${PWD}/.conda
if [ "$ENVIRONMENT" != "production" ];
  then exec uvicorn --workers 1 --host 0.0.0.0 --port 80 main:app;
else exec gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 main:app;
fi;