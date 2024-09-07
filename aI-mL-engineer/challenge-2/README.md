# Garment Factory Production Output Forecasting

## Overview

This project involves creating a time series model to forecast daily production output for a garment factory. The model considers various factors such as worker attendance, power availability, and seasonal trends. It is designed to handle missing data due to power outages, incorporate external factors like load shedding schedules and holiday calendars, and provide daily predictions for the next 30 days, including uncertainty estimates.

## Approach and Methodology

1. **Data Preprocessing**:
   - Handle missing data using interpolation.
   - Incorporate external factors such as load shedding hours and holiday schedules.
   - Prepare the data for modeling by converting columns and handling missing values.

2. **Model Training**:
   - Use the `Prophet` library for time series forecasting.
   - Include external regressors: Worker Attendance, Power Availability Hours, Holiday, and Load Shedding Hours.

3. **Prediction**:
   - Predict the next 30 days of production output.
   - Provide uncertainty estimates with the predictions.

## Technologies, Libraries, and Frameworks Used

- **Python**: Programming language used for implementation.
- **Pandas**: Data manipulation and analysis.
- **Prophet**: Time series forecasting.
- **Pickle**: Model serialization.

## Instructions for Setting Up the Environment and Running the Code

1. **Clone the Repository**: Clone the project repository to your local machine.
    ```bash
    git clone <https://github.com/sojib96/Coding-Challenges.git>
    cd <aI-mL-engineer>
    cd <challenge-2>
    ```

2. **Create a Virtual Environment**: Set up a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

4. **Install Dependencies**: Install the required Python libraries.
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Training Pipeline**: Train the model with historical data.
    ```bash
    python training.py
    ```

6. **Run the Prediction Pipeline**: Use the trained model to forecast the next 30 days.
    ```bash
    python inference.py
    ```

## Assumptions and Limitations
- **Waiting**: Ensure that the `training.py` file has finished executing before running the `inference.py` file.
- **Data Replacement**: Replace the `latest_data.csv` file with your actual data points. The inference pipeline will also handle any missing values in the provided data.

## Results and Performance Metrics

The trained model will output predictions for the next 30 days, including uncertainty estimates. The result will be displayed in the command line when you run the Inference script.

**Expected Output:**

```plaintext
           ds        yhat  yhat_lower   yhat_upper
0  2024-01-01  976.345748  830.615719  1103.295864
1  2024-01-02  974.322283  840.472778  1118.987849
2  2024-01-03  992.038597  847.317409  1145.620063
3  2024-01-04  983.440320  840.339995  1125.500716
4  2024-01-05  975.852677  840.560721  1132.318671
5  2024-01-06  983.588025  840.786977  1125.454896
6  2024-01-07  979.537954  846.584754  1122.390594
7  2024-01-08  975.897507  837.556410  1116.052895
8  2024-01-09  973.874042  831.583980  1111.718152
9  2024-01-10  991.590355  853.576065  1128.174702
10 2024-01-11  982.992078  839.805308  1127.118311
11 2024-01-12  975.404436  824.008024  1118.313113
12 2024-01-13  983.139784  849.862080  1128.304119
13 2024-01-14  979.089713  841.366125  1120.454937
14 2024-01-15  975.449266  841.238324  1125.687095
15 2024-01-16  973.425800  829.008290  1110.609293
16 2024-01-17  991.142114  858.293364  1128.451694
17 2024-01-18  982.543837  844.519866  1135.138937
18 2024-01-19  974.956195  830.856779  1120.120626
19 2024-01-20  982.691542  842.291831  1122.754872
20 2024-01-21  978.641472  831.574218  1122.389464
21 2024-01-22  975.001025  835.528799  1116.572793
22 2024-01-23  972.977559  825.354598  1112.195489
23 2024-01-24  990.693873  848.817565  1123.553625
24 2024-01-25  982.095596  842.646197  1126.248781
25 2024-01-26  974.507954  836.115341  1127.485218
26 2024-01-27  982.243301  858.723710  1128.658301
27 2024-01-28  978.193231  848.559166  1110.225507
28 2024-01-29  974.552783  826.171393  1113.907259
29 2024-01-30  972.529318  823.720055  1116.207386
