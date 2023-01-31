from rest_framework.test import APITestCase
from rest_framework import status
from rrms_web_app.views import LastValues

# Create your tests here.
class CurrentStatusTests(APITestCase):
    def test_take_current(self):
        response = self.client.get("/current/")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_take_current(self):
        response = self.client.post("/current/", {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_take_last_values(self):
        response = self.client.get("/last_values/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_take_last_values(self):
        response = self.client.post("/last_values/", {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_splitArrayBykey_IsHaveArray_ReturnCorrectArray():
        #arrange
        testKey = "testkey"
        testArray = ["testkey":"test", "testkey1":"test", "testkey2":"test"]
        expectedArray =  ["testkey": "test"]
        lastValues = LastValues()

        #act
        result = lastValues._splitArrayBykey(expectedArray, testKey)

        #assert
        self.assertEquals(expectedArray, lastValues)
        testArray, testKey

    def test_splitArrayBykey_IsArrayEmpty_ReturnEmptyArray():
        #arrange
        expectedArray = []
        lastValues = LastValues()
        
        #act
        result = lastValues._splitArrayBykey(expectedArray, "")

        #assert
        self.assertEquals(expectedValue, result)