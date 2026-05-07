# End-to-End Sales Forecasting System

## Objective
Forecast next 8 weeks of sales for each state using historical sales data.

## Features
- Missing value handling
- Time series preprocessing
- Feature engineering
- Multiple forecasting models
- Automatic best model selection
- REST API deployment

## Models Used
1. ARIMA
2. Prophet
3. XGBoost
4. LSTM

## Engineered Features
- lag_1
- lag_7
- lag_30
- rolling_mean_7
- rolling_std_7
- month
- quarter
- year
- week_of_year

## API
FastAPI REST API

### Run API

```bash
cd api
uvicorn app:app --reload