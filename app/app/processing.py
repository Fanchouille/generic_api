import numpy as np

# Here add custom code to add some preproc on data
class Processor:
    def __init__(self):
        return

    def apply_preprocessing(self, data):
        return np.array([data[key] for key in data.fields.keys()]).T

    def get_prediction(model, preprocessor, input_params):
        x = preprocessor.apply_preprocessing(input_params)
        y = model.predict(x)
        probs = model.predict_proba(x).tolist()
        return [{'prediction': int(pred), 'probability': probs[enum]} for enum, pred in enumerate(y)]