# Generic API
This a dockerized API to expose a scikit model with fastAPI (dummy model with Iris dataset).
Based on [this docker image](https://github.com/tiangolo/uvicorn-gunicorn-docker)

## Structure 
#### *API endpoints*
>/app/app/main.py 
#### *Schemas of inputs and outputs*
>/app/app/schemas.py
#### *Custom preprocessing and get_prediction function*
>/app/app/processing.py
#### *Pickled scikit model*
>/app/model/model.pkl

## What do I need to do ?
Clone repo

Change inputs format in schemas.py (& outputs if needed)

Change processing code if needed.

Train & pickle (with joblib) a scikit model and store it in app/model folder.

Build & run docker image (see below)

## Build & Run :
### *Build image :*
* `cd generic_api`
* `docker build -t generic_api .`

### *Run image :*
#### *remove -d to keep CLI attached*
`docker run -d -p 80:80 generic_api`

#### *Dev mode (1 worker) : run with live reload with local folder as volume*
`docker run -d -p 80:80 -v $(pwd)/app:/app generic_api /start-reload.sh`


## Access :
Your API documentation is available at [http://127.0.0.1/docs](http://127.0.0.1/docs)