## Challenge 2: Time Series Forecasting for Production Planning

### Scenario:
You need to create a model to forecast daily production output for a garment factory, considering factors like worker attendance, power availability, and seasonal trends.

### Task:
Using historical data, create a time series model that:
1. Handles missing data (common due to power outages)
2. Incorporates external factors (e.g., load shedding schedules, holiday calendar)
3. Provides daily predictions for the next 30 days
4. Includes uncertainty estimates in the predictions

### Sample Input:
Use production_data.csv as sample input

### Expected Output:
A trained model and a function that takes the latest data point and returns predictions for the next 30 days, including uncertainty estimates.
