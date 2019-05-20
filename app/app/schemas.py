from pydantic import BaseModel
from typing import List


# Model inputs for post request
class ModelUnitInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Model inputs for post request
class ModelInputs(BaseModel):
    inputs: List[ModelUnitInput]


# Model outputs
# Unitary result
class ModelOutputs(BaseModel):
    prediction: int
    probabilities: List[float]


# List of unitary result
class ModelOutputsList(BaseModel):
    outputs: List[ModelOutputs]
