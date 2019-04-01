from fastapi import FastAPI
from sklearn.externals import joblib
from pydantic import  BaseModel


# define model for post request
class ModelParams(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()

model = joblib.load("model/iris_model.pkl")

def get_prediction(sepal_length, sepal_width, petal_length, petal_width):
    x = [[sepal_length, sepal_width, petal_length, petal_width]]
    y = model.predict(x)[0]
    prob = model.predict_proba(x)[0].tolist()
    return {'prediction': int(y), 'probability': prob}

@app.post("/predict-post/")
def post_predict(params: ModelParams):
    param_dict = params.dict()
    pred = get_prediction(**param_dict)
    return pred