from pydantic import BaseModel
from typing import List


# Model inputs for post request
class ModelInputs(BaseModel):
    sepal_length: List[float]
    sepal_width: List[float]
    petal_length: List[float]
    petal_width: List[float]


# Model outputs
# Unitary result
class ModelOutputs(BaseModel):
    prediction: int
    probabilities: List[float]


# List of unitary result
class ModelOutputsList(BaseModel):
    results: List[ModelOutputs]