import numpy as np
import pandas as pd
from sklearn.metrics import matthews_corrcoef
import logging
from varname import nameof

class DataExplorationService():
    def getCorrelationCoefficient(self, arrayX, arrayY):        
        try:
            if(arrayX is None or len(arrayX) == 0): # To DO create Guard
                self.logger.error(f"""exeption behavior in service: {nameof(DataExplorationService)} 
                method: {nameof(self.getCorrelationCoefficient)} value: {arrayX} None or empty""")
                return None
            
            if(arrayY is None or len(arrayY) == 0):
                self.logger.error(f"""exeption behavior in service: {nameof(PredictionService)} 
                method: {nameof(self.getCorrelationCoefficient)} value: {arrayY} None or empty""")
                return None
            
            arrayNumPyX = np.array(arrayX)
            arrayNumPyY = np.array(arrayY)
            coef = np.corrcoef(arrayNumPyX, arrayNumPyY)
            
            return float(coef[0][1])
        except Exception as e:
            self.logger.error(f'An exception occurred in {nameof(DataExplorationService)} method {nameof(self.getUniqueValuesAndAmount)}. exeption - {e} ')
        return None
      

    def getUniqueValuesAndAmount(self, array):
        try:
            if(array is None or len(array) == 0):
                self.logger.error(f"""exeption behavior in service: {nameof(DataExplorationService)} 
                method: {nameof(self.getUniqueValuesAndAmount)} value: {array} None or empty""")
                return None
            
            values, amounts =  np.unique(array, return_counts=True)
            values = list(values)
            amounts = list(amounts)

            responseV = []
            responseA = []

            for i in range(len(values)):
                responseV.append(float(values[i]))

            for i in range(len(amounts)):
                responseA.append(int(amounts[i]))

            return responseV, responseA
        except Exception as e:
            self.logger.error(f'An exception occurred in {nameof(DataExplorationService)} method {nameof(self.getUniqueValuesAndAmount)}. exeption - {e} ')
        return None