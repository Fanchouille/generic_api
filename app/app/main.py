from fastapi import FastAPI
from starlette.requests import Request
import time
import joblib
from .schemas import ModelInputs, ModelOutputsList
from .processing import Processor

# Instantiate app
app = FastAPI()

# Load model - MODIFY NAME OF MODEL if needed
model = joblib.load("model/model.pkl")

# Instantiate Preprocessor - MODIFY PROCESSOR CLASS (see processing.py) AND schemas of inputs/outputs (see schemas.py)
processor = Processor()


# POST endpoint
@app.post("/predict-post/", response_model=ModelOutputsList)
def post_predict(inputs: ModelInputs):
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
