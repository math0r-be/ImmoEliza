import pickle
import pandas as pd
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../ml/model.pkl")
FEATURES_PATH = os.path.join(os.path.dirname(__file__), "../ml/model_features.csv")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

feature_names = pd.read_csv(FEATURES_PATH, nrows=1).columns.tolist()

def predict_price(features: dict) -> float:
    df_input = pd.DataFrame([features])
    df_input = df_input.reindex(columns=feature_names, fill_value=0)
    prediction = model.predict(df_input)[0]
    return round(prediction, 2)
