from django.test import TestCase
from rrms_web_app.models import MainData
from django.utils import timezone

class MainDataModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        MainData.objects.create(temperature=12.3, pressure=60121, humidity=69, timeaData=str(timezone.now()))

    def test_MainModel_MainModelHasTemperature_ReturnTrue(self):
        #arrange
        expectedName = 'temperature'
        mainData = MainData.objects.last()
        
        #act
        field_label = mainData._meta.get_field(expectedName).verbose_name

        #asser
        self.assertEquals(field_label, expectedName)

    def test_MainModel_MainModelHasPressure_ReturnTrue(self):
        #arrange
        expectedName = 'pressure'
        mainData = MainData.objects.last()
        
        #act
        field_label = mainData._meta.get_field(expectedName).verbose_name

        #asser
        self.assertEquals(field_label, expectedName)

    def test_MainModel_MainModelHasHumidity_ReturnTrue(self):
        #arrange
        expectedName = 'humidity'
        mainData = MainData.objects.last()
        
        #act
        field_label = mainData._meta.get_field(expectedName).verbose_name

        #asser
        self.assertEquals(field_label, expectedName)

    def test_MainModel_MainModelHastimeaData_ReturnTrue(self):
        #arrange
        expectedName = 'timeaData'
        mainData = MainData.objects.last()
        
        #act
        field_label = mainData._meta.get_field(expectedName).verbose_name

        #asser
        self.assertEquals(field_label, expectedName)

    def test_MainModel_HasCorretData_ReturnTrue(self):
        #arrange
        expectedTemperature = 12.3
        expectedPressure = 60121.0
        expectedHumidity = 69.0
        
        #act
        mainData = MainData.objects.last()
        
        #asser
        self.assertEquals(True, self._checkMainModelData(mainData, expectedTemperature, expectedPressure, expectedHumidity))

  
    def _checkMainModelData(self, mainModel, temperature, pressure, humidity):
        return mainModel.temperature == temperature and mainModel.pressure == pressure and mainModel.humidity == humidity