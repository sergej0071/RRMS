from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import datetime
import numpy as np
import pandas as pd
import logging
from varname import nameof

class PredictionService():
    def __init__(self):
        self.logger = logging.getLogger('error_logger')
    def getPredictionValue(self, value, timePeriod, predictAmount = 10, degreeP = 3):

        if(value is None or len(value) == 0):
            self.logger.error(f"""exeption behavior in service: {nameof(PredictionService)} 
            method: {nameof(self.getPredictionValue)} value: {value} None or empty""")
            return None

        if(timePeriod is None or timePeriod <= 0):
            self.logger.error(f"""exeption behavior in service: {nameof(PredictionService)} \ 
            method: {nameof(self.getPredictionValue)} timePeriod: {timePeriod} None or <= 0""")
            return None

        if(predictAmount is None or predictAmount <= 0):
            self.logger.error(f"""exeption behavior in service: {nameof(PredictionService)} \
            method: {nameof(self.getPredictionValue)} predictAmount: {predictAmount} None or <= 0""")
            return None

        if(degreeP is None or degreeP <= 0):
            self.logger.error(f"""exeption behavior in service: {nameof(PredictionService)} \
            method: {nameof(self.getPredictionValue)} degreeP: {degreeP} None or <= 0 """)
            return None

        conditionalTime = [i for i in range(1, len(value) + 1, timePeriod)]
        arrayTime = np.array(conditionalTime)
        dataFrameTime = pd.DataFrame(arrayTime)
        timeValue = dataFrameTime.iloc[:, 0:1].values

        arrayValue = np.array(value)
        DataFrameValue = pd.DataFrame(arrayValue)
        valueD = DataFrameValue.iloc[:, 0].values

        poly_reg = PolynomialFeatures(degree = degreeP)
        value_poly = poly_reg.fit_transform(timeValue)
        lin_reg = LinearRegression()
        lin_reg.fit(value_poly, valueD)

        for it in range(len(value), len(value) + predictAmount, timePeriod):
           value.append(lin_reg.predict(poly_reg.fit_transform([[it]]))[0])

        return value

    def modifyPredictedTime(self, time, timePeriod, predictAmount = 10):

        if(time is None or len(time) == 0):
            self.logger.error(f"""exeption behavior in service: {nameof(PredictionService)} \
            *method: {nameof(self.getPredictionValue)} time: {time} None or empty""")
            return None

        if(timePeriod is None or timePeriod <= 0):
            self.logger.error(f"""exeption behavior in service: {nameof(PredictionService)} \
            *method: {nameof(self.getPredictionValue)} timePeriod: {timePeriod} None or <= 0""")
            return None

        if(predictAmount is None or predictAmount <= 0):
            self.logger.error(f"""exeption behavior in service: {nameof(PredictionService)} \
            *method: {nameof(self.getPredictionValue)} predictAmount: {predictAmount} None or <= 0""")
            return None

        seconds = [i for i in range(1, predictAmount + 1, timePeriod)]
        lastTick = time[-1]

        for it in seconds:
            time.append(lastTick + datetime.timedelta(seconds=it))

        return time