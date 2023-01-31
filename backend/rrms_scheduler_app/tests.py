from django.test import TestCase
from rrms_scheduler_app.predictionService import PredictionService
from rrms_web_app.models import MainData
from django.utils import timezone

class PredictionServiceTests(TestCase):
#region getPredictionValue def getPredictionValue(self, value, timePeriod, predictAmount = 10, degreeP = 8):  

    def test_getPredictionValue_IsValueNone_ReturnNone(self):
        #arrange
        expectedValue = None
        timePeriod = 1
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(expectedValue, timePeriod)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_getPredictionValue_IsValueEmty_ReturnNone(self):
        #arrange
        arrayValue = []
        expectedValue = None
        timePeriod = 1
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(arrayValue, timePeriod)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_getPredictionValue_IsTimePeriodZero_ReturnNone(self):
        #arrange
        expectedValue = None
        valueArray = [MainData(), MainData(), MainData()]
        timePeriod = 0
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(valueArray, timePeriod)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_getPredictionValue_IsTimePeriodNone_ReturnNone(self):
        #arrange
        expectedValue = None
        valueArray = [MainData(), MainData(), MainData()]
        timePeriod = None
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(valueArray, timePeriod)

        #assert
        self.assertEquals(expectedValue, resultValue)
    
    def test_getPredictionValue_IsPredictAmountNone_ReturnNone(self):
        #arrange
        expectedValue = None
        valueArray = [MainData(), MainData(), MainData()]
        timePeriod = 1
        predictAmount = None
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(valueArray, timePeriod, predictAmount)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_getPredictionValue_IsPredictAmountZero_ReturnNone(self):
        #arrange
        expectedValue = None
        valueArray = [MainData(), MainData(), MainData()]
        timePeriod = 1
        predictAmount = 0
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(valueArray, timePeriod, predictAmount)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_getPredictionValue_IsPredictDegreePZero_ReturnNone(self):
        #arrange
        expectedValue = None
        valueArray = [MainData(), MainData(), MainData()]
        timePeriod = 1
        predictAmount = 1
        degreeP = 0
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(valueArray, timePeriod, predictAmount, degreeP)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_getPredictionValue_IsPredictAmountNone_ReturnNone(self):
        #arrange
        expectedValue = None
        valueArray = [MainData(), MainData(), MainData()]
        timePeriod = 1
        predictAmount = 1
        degreeP = None
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(valueArray, timePeriod, predictAmount,degreeP)

        #assert
        self.assertEquals(expectedValue, resultValue)

#end getPredictionValue
    def test_modifyPredictedTime_IsValueTimeNone_ReturnNone(self):
        #arrange
        expectedValue = None
        time = None
        timePeriod = 1
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(time, timePeriod)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_modifyPredictedTime_IsValueTimeEmpty_ReturnNone(self):
        #arrange
        expectedValue = None
        time = []
        timePeriod = 1
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(time, timePeriod)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_modifyPredictedTime_IsTimePeriodNone_ReturnNone(self):
        #arrange
        expectedValue = None
        time = [timezone.now(), timezone.now(), timezone.now()]
        timePeriod = None
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(time, timePeriod)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_modifyPredictedTime_IsTimePeriodZero_ReturnNone(self):
        #arrange
        expectedValue = None
        time = [timezone.now(), timezone.now(), timezone.now()]
        timePeriod = 0
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(time, timePeriod)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_modifyPredictedTime_IsPredictAmountNone_ReturnNone(self):
        #arrange
        expectedValue = None
        time = [timezone.now(), timezone.now(), timezone.now()]
        timePeriod = 1
        amount = None
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(expectedValue, timePeriod, amount)

        #assert
        self.assertEquals(expectedValue, resultValue)

    def test_modifyPredictedTime_IsPredictAmountZero_ReturnNone(self):
        #arrange
        expectedValue = None
        time = [timezone.now(), timezone.now(), timezone.now()]
        timePeriod = 1
        amount = 0
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(expectedValue, timePeriod, amount)

        #assert
        self.assertEquals(expectedValue, resultValue)

    
    def test_modifyPredictedTime__ReturnNone(self):
        #arrange
        expectedValue = None
        time = [timezone.now(), timezone.now(), timezone.now()]
        timePeriod = 1
        amount = 0
        predictionService = PredictionService()
        
        #act
        resultValue = predictionService.getPredictionValue(expectedValue, timePeriod, amount)

        #assert
        self.assertEquals(expectedValue, resultValue)

#end modifyPredictedTime