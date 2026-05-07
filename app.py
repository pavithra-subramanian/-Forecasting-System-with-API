from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(
    title="Sales Forecasting API",
    description="Forecast next 8 weeks sales using ML models",
    version="1.0.0"
)

# Load model
model = joblib.load("../models/best_model.pkl")


@app.get("/")
def home():
    return {
        "message": "Sales Forecast API Running Successfully"
    }


@app.get("/predict")
def predict():

    sample_data = pd.DataFrame({
        'lag_1': [500000000],
        'lag_7': [480000000],
        'lag_30': [470000000],
        'rolling_mean_7': [490000000],
        'rolling_std_7': [10000000],
        'month': [12],
        'quarter': [4],
        'year': [2023],
        'week_of_year': [50]
    })

    prediction = model.predict(sample_data)

    return {
        "forecast": float(prediction[0])
    }