import pandas as pd
import pickle

class PredictionPipeline:
    def __init__(self, modelPath, dataPath):
        self.modelPath = modelPath
        self.dataPath = dataPath
        self.model = None
        self.latestData = None

    def loadModel(self):
        with open(self.modelPath, 'rb') as file:
            self.model = pickle.load(file)

    def loadData(self):
        self.latestData = pd.read_csv(self.dataPath, parse_dates=['Date'])
        self.latestData.rename(columns={'Date': 'ds'}, inplace=True)

    def handleMissingValues(self):
        self.latestData.interpolate(method='linear', inplace=True)
        self.latestData.fillna(method='bfill', inplace=True)

    def prepareFutureDf(self):
        futureDates = pd.date_range(start=self.latestData['ds'].max() + pd.Timedelta(days=1), periods=30)
        futureDf = pd.DataFrame({'ds': futureDates})

        for col in ['Worker Attendance', 'Power Availability Hours', 'Holiday', 'Load Shedding Hours']:
            futureDf[col] = self.latestData[col].mean()

        return futureDf

    def predictNext30Days(self):
        self.handleMissingValues()
        futureDf = self.prepareFutureDf()
        forecast = self.model.predict(futureDf)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    def run(self):
        self.loadModel()
        self.loadData()
        forecast = self.predictNext30Days()
        print(forecast)

if __name__ == '__main__':
    pipeline = PredictionPipeline('prophet_model.pkl', 'latest_data.csv')
    pipeline.run()
