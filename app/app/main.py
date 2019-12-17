from fastapi import FastAPI
from starlette.requests import Request
import time
import joblib
from .schemas import ModelInputs, ModelOutputsList
from .processing import Processor
# Scheduler
import pytz
from apscheduler.schedulers.background import BackgroundScheduler

# Instantiate app
app = FastAPI()

# model will be a global var that can but hot reloaded
model = None


def update_global_vars():
    global model
    # Load model - here you can fetch model where it is stored (cloud / local etc)
    model = joblib.load("./model/model.pkl")

    return model


@app.on_event('startup')
def startup_event():
    # First loading of model...
    update_global_vars()
    # ...then schedule it !
    scheduler = BackgroundScheduler(timezone=pytz.utc)
    scheduler.start()
    # Specify the update rate of the model
    # see doc here https://apscheduler.readthedocs.io/en/latest/userguide.html#adding-jobs
    # you can also use cron like
    scheduler.add_job(update_global_vars, trigger="interval", seconds=30, id="load_model", replace_existing=True)


# Instantiate Preprocessor - MODIFY PROCESSOR CLASS (see processing.py) AND schemas of inputs/outputs (see schemas.py)
processor = Processor()


# POST endpoint
@app.post("/predict-post/", response_model=ModelOutputsList)
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
