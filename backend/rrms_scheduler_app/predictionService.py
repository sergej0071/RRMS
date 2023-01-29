from sklearn.linear_model import LinearRegression
import datetime
import numpy as np
import pandas as pd

class PredictionService():        
    def getPredictionValue(self, value, timePeriod, predictAmount = 10, degreeP = 8):  

        conditionalTime = [i for i in range(1, len(value) + 1, timePeriod)]
        arrayTime = np.array(conditionalTime)
        dataFrameTime = pd.DataFrame(arrayTime)
        timeValue = dataFrameTime.iloc[:, 0:1].values

        arrayValue = np.array(value)
        DataFrameValue = pd.DataFrame(arrayValue)
        valueD = DataFrameValue.iloc[:, 0].values

        lin_reg = LinearRegression()
        lin_reg.fit(timeValue, valueD)

        for it in range(len(value), len(value) + predictAmount, timePeriod):
           value.append(lin_reg.predict[[it]])[0]

        return value

    def modifyPredictedTime(self, time, timePeriod, predictAmount = 10):
        
        if(len(time) == 0):
            return time

        seconds = [i for i in range(1, predictAmount + 1, timePeriod)]
        lastTick = time[-1]

        for it in seconds:
            time.append(lastTick + datetime.timedelta(seconds=it))

        return time