from fastapi import FastAPI
import joblib
from .schemas import ModelInputs, ModelOutputsList
from .processing import Processor

# Instantiate app
app = FastAPI()

# Load model - MODIFY NAME OF MODEL
model = joblib.load("model/iris_model.pkl")

# Instantiate Preprocessor - MODIFY PROCESSOR CLASS (see processing.py) AND schemas of inputs/outputs (see schemas.py)
processor = Processor()

# POST endpoint
@app.post("/predict-post/", response_model=ModelOutputsList)
def post_predict(input_params: ModelInputs):
    preds = processor.get_prediction(model, input_params)
    return preds