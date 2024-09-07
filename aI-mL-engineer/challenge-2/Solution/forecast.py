import pandas as pd
from prophet import Prophet
import numpy as np
import pickle
import argparse
import gdown
import os
from tabulate import tabulate
import warnings

# Ignore deprecation warnings for cleaner output
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Argument Parsing Setup
parser = argparse.ArgumentParser(description="Production Output Forecasting using Prophet.")
parser.add_argument("--model-path", default="model.pkl", help="Path to the trained model file.")
parser.add_argument("--target-path", default="production_data.csv", help="Path to the input CSV file with historical data.")
parser.add_argument("--result-path", default="result.csv", help="Path to save the forecast results.")
parser.add_argument("--display", default=True, help="Whether to display the forecast results in the terminal.")
args = parser.parse_args()

# Model path argument
MODEL_PATH = args.model_path

# Download model file from Google Drive if it doesn't exist locally
if not os.path.isfile(MODEL_PATH):
    url = 'https://drive.google.com/uc?id=1vVNYO9bh9mo8FLS6fCWGU_ZtGKvZf4Zu'
    print(f"Model file not found. Downloading from {url}")
    gdown.download(url, MODEL_PATH, quiet=False)

# Load the trained model from the pickle file
with open(MODEL_PATH, 'rb') as fin:
    model = pickle.load(fin)
print("### Model loaded successfully ###")

def forecast_csv(target_df, result_path="result.csv", display=True):
    """
    Function to forecast production output using a pre-trained Prophet model.

    Parameters:
        target_df (DataFrame): Input dataframe containing historical data.
        result_path (str): Path to save the forecast result as CSV.
        display (bool): Whether to display the forecast results in the terminal.
    """
    # Ensure date is in the correct format and sort the data
    target_df['Date'] = pd.to_datetime(target_df['Date'], errors='coerce')
    target_df = target_df.sort_values('Date')
    target_df.rename(columns={'Date': 'ds'}, inplace=True)  # Rename 'Date' column to 'ds' for Prophet compatibility

    # Generate future dates for forecasting (30 days into the future)
    future = model.make_future_dataframe(periods=30)

    # Simulate additional variables (Worker Attendance, Power Availability, and Holidays)
    future['Worker Attendance'] = np.random.normal(target_df['Worker Attendance'].mean(), target_df['Worker Attendance'].std(), len(future))
    future['Power Availability Hours'] = np.random.normal(target_df['Power Availability Hours'].mean(), target_df['Power Availability Hours'].std(), len(future))
    future['Holiday'] = np.random.choice([0, 1], size=len(future), p=[0.9, 0.1])  # Randomly assign holidays (10% probability)

    # Generate predictions (yhat) for the future dates
    forecast = model.predict(future)[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30)  # Forecast for the next 30 days
    
    # Append the production output to the future dataframe
    future = future.tail(30)
    future['Production Output'] = forecast['yhat']
    
    # Combine historical data and forecasted results
    result_df = pd.concat([target_df, future])
    result_df.rename(columns={'ds': 'Date'}, inplace=True)  # Rename 'ds' back to 'Date' for readability

    # Save the results to a CSV file
    result_df.to_csv(result_path, index=False)
    print(f"### Results saved to {result_path} ###")
    
    # Optionally display the forecast in a tabular format in the terminal
    if display:
        print(
            tabulate(
                forecast,
                headers=forecast.columns,
                floatfmt=".5f",
                showindex=False,
                tablefmt="psql",
            )
        )

if __name__ == "__main__":
    # Load the input CSV and perform the forecasting
    try:
        target_df = pd.read_csv(args.target_path)
        forecast_csv(target_df, args.result_path, args.display)
    except FileNotFoundError:
        print(f"Error: File {args.target_path} not found.")
    except Exception as e:
        print(f"Error processing CSV: {e}")
