import pandas as pd
from prophet import Prophet

# Load your data
data = pd.read_csv('production_data.csv')

# Handle missing values
# Forward fill to handle NaNs by carrying the last valid observation forward
data['Production Output'] = data['Production Output'].ffill()
data['Worker Attendance'] = data['Worker Attendance'].ffill()
data['Power Availability Hours'] = data['Power Availability Hours'].ffill()

# Backfill to handle any remaining NaNs by carrying the next valid observation backward
data['Production Output'] = data['Production Output'].bfill()
data['Worker Attendance'] = data['Worker Attendance'].bfill()
data['Power Availability Hours'] = data['Power Availability Hours'].bfill()

# Alternatively, fill any remaining NaNs with the mean of the column
data['Production Output'].fillna(data['Production Output'].mean(), inplace=True)
data['Worker Attendance'].fillna(data['Worker Attendance'].mean(), inplace=True)
data['Power Availability Hours'].fillna(data['Power Availability Hours'].mean(), inplace=True)

# Preparing data for Prophet
data_prophet = pd.DataFrame()
data_prophet['ds'] = pd.to_datetime(data['Date'])  # Convert your date column to datetime format
data_prophet['y'] = data['Production Output']  # Use the target column for prediction

# Initialize Prophet model
model = Prophet()
model.fit(data_prophet)

# Create future dates for forecasting
future = model.make_future_dataframe(periods=30)  # Adjust periods as needed for forecasting
forecast = model.predict(future)

# Visualize the forecast
fig = model.plot(forecast)
fig.show()

# Visualize forecast components
fig2 = model.plot_components(forecast)
fig2.show()
