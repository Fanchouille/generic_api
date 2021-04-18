# Generic API
This a dockerized API to expose a scikit model with fastAPI (dummy model with Iris dataset).

## Development
### Anaconda local environment support

Install Anaconda local environment as below:
```bash
./install.sh
```

Set Anaconda local environment as `${PWD}/.conda` as Python interpreter of the project (using PyCharm)

## Structure 
#### *API endpoints*
>main.py 
#### *Schemas of inputs and outputs*
>schemas.py
#### *Custom preprocessing and get_prediction function*
>processing.py
#### *Pickled or joblib scikit model*
>models/
#### *Configuration files*
>config/

## What do I need to do ?
Clone repo

Change inputs format in schemas.py (& outputs if needed)

Change processing code if needed.

Train & pickle (with joblib) a scikit model and store it in app/model folder. 
**Be sure to use the same version of scikit during training & inference.**

Build & run docker image (see below)

## Build & Run :
### *Build image :*
* `cd generic_api`
* `docker build -t generic_api .`

### *Run image :*
#### *remove -d to keep CLI attached*

`docker run -d -p 80:80 generic_api`

## Access :
Your API documentation is available at [http://127.0.0.1/docs](http://127.0.0.1/docs)

## Deployment :

See DEPLOYMENT.md for simple Azure deployment.
