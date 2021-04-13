# coding: utf-8
from fastapi import FastAPI
from starlette.requests import Request
import time
import joblib
import yaml
import os
from schemas import ModelInputs, ModelOutputsList
from processing import Processor
import pytz

# Get environment from env variable
environment = os.environ["ENVIRONMENT"] if (
            "ENVIRONMENT" in os.environ and os.environ["ENVIRONMENT"] != "") else "development"
print("ENVIRONMENT : {}".format(environment))

# Load configuration from ENVIRONMENT variable
with open("./config/{}.yml".format(environment), "r") as configuration_file:
    config = yaml.load(configuration_file, Loader=yaml.FullLoader)
print(config)
# Instantiate app
app = FastAPI()
# model will be a global var that can be hot reloaded
model = None


@app.on_event('startup')
def startup_event():
    global model
    print("Loading model from: [{}]").format(config["model_path"])
    model = joblib.load(config["model_path"])


# Instantiate Preprocessor - MODIFY PROCESSOR CLASS (see processing.py) AND schemas of inputs/outputs (see schemas.py)
processor = Processor()


# POST endpoint
@app.post("/predict/", response_model=ModelOutputsList)
async def post_predict(inputs: ModelInputs):
    outputs = processor.get_prediction(model, inputs)
    return outputs


# Middleware to add time info
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
