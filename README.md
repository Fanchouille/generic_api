# Generic API

This a dockerized API to expose a scikit model with fastAPI.

Based on https://github.com/tiangolo/uvicorn-gunicorn-docker

# Structure 

### *API endpoints are in main but you may add your utils in 'app/app' folder*

/app/app/main.py 

### *Pickled model is in 'app/model' folder*

/app/model/your_model.pkl

# Run this :

## *Build image :*

cd generic_api

docker build -t generic_api .

## *Run image :*

### *remove -d to keep CLI attached*

'''docker run -d -p 80:80 generic_api'''

### *Dev mode : run with live reload | -v $(pwd) to use local folder as volume*

docker run -d -p 80:80 -v $(pwd) generic_api /start-reload.sh
