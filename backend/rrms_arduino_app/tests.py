from rest_framework.test import APITestCase
from rest_framework import status
from rrms_arduino_app.arduinoService import ArduinoService

# Create your tests here.
class ArduinoServiceTests(APITestCase):
    def test_getArduinoModel_arduinoConnectionIsNone_returnNone(self):
        #arrange
        _arduinoService = ArduinoService()
        expectedResult = None
        
        #act
        result = _arduinoService.getArduinoModel()

        #assert
        self.assertEqual(expectedResult, result)