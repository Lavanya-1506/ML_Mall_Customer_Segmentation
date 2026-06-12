import joblib
import numpy as np


class CustomerPredictor:

    def __init__(self):

        self.scaler = joblib.load(
            "../models/scaler.pkl"
        )

        self.model = joblib.load(
            "../models/kmeans_model.pkl"
        )

    def predict(
        self,
        age,
        income,
        score
    ):

        data = np.array(
            [
                [
                    age,
                    income,
                    score
                ]
            ]
        )

        scaled_data = self.scaler.transform(
            data
        )

        cluster = self.model.predict(
            scaled_data
        )[0]

        segment_names = {

            0: "Premium Customers",

            1: "Budget Customers",

            2: "Young High Spenders",

            3: "Average Customers",

            4: "Careful Customers"

        }

        return segment_names.get(
            cluster,
            "Unknown"
        )


if __name__ == "__main__":

    predictor = CustomerPredictor()

    result = predictor.predict(
        age=25,
        income=80,
        score=90
    )

    print(result)