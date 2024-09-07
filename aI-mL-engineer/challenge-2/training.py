import pandas as pd
from prophet import Prophet
import pickle

class TrainingPipeline:
    def __init__(self, data_filepath, model_filepath):
        self.data_filepath = data_filepath
        self.model_filepath = model_filepath
        self.df = None
        self.model = None

    def load_data(self):
        self.df = pd.read_csv(self.data_filepath, parse_dates=['Date'])
        return self

    def preprocess_data(self):
        max_power_hours = 23
        self.df['Load Shedding Hours'] = (max_power_hours - self.df['Power Availability Hours']) + self.df['Holiday'] #penalty for 
        self.df = self.df.interpolate(method='linear')
        self.df['y'] = pd.to_numeric(self.df['Production Output'], errors='coerce')
        self.df.rename(columns={'Date': 'ds'}, inplace=True)
        return self

    def train_model(self):
        self.model = Prophet()
        self.model.add_regressor('Worker Attendance')
        self.model.add_regressor('Power Availability Hours')
        self.model.add_regressor('Holiday')
        self.model.add_regressor('Load Shedding Hours')
        
        self.model.fit(self.df)
        return self

    def save_model(self):
        with open(self.model_filepath, 'wb') as file:
            pickle.dump(self.model, file)
        return self

    def run_pipeline(self):
        self.load_data()
        self.preprocess_data()
        self.train_model()
        self.save_model()

def main():
    pipeline = TrainingPipeline('production_data.csv', 'prophet_model.pkl')
    pipeline.run_pipeline()

if __name__ == '__main__':
    main()
