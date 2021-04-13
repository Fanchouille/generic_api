import numpy as np


class Processor:
    def __init__(self):
        return

    def apply_preprocessing(self, data):
        """

        :param data: raw data from API with ModelInputs schema (see schemas.py)
        :return: preprocessed data
        """
        # Just get list of feature as a numpy matrix
        # Add custom code to add preproc on data

        # List of dict inputs
        inputs = data.dict()["inputs"]

        # Build array of features
        return np.array([[record[key] for key in record.keys()] for record in inputs])

    def get_prediction(self, model, data):
        """

        :param model: a trained scikit model
        :param data: raw data from API with ModelInputs schema (see schemas.py)
        :return: a dict with results : a list of prediction / probabilities
        """
        x = self.apply_preprocessing(data)
        y = model.predict(x).tolist()
        probs = model.predict_proba(x).tolist()
        # Be sure the output of get_prediction matches ModelOutputsList (see schemas.py)
        return {'outputs': [{'prediction': int(pred), 'probabilities': probs[enum]} for enum, pred in enumerate(y)]}
