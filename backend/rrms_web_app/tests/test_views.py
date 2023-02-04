from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class CurrentStatusTests(APITestCase):

    def test_wrong_take_current(self):
        response = self.client.post("/current/", {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_take_last_values(self):
        response = self.client.get("/last_values/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_take_last_values(self):
        response = self.client.post("/last_values/", {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)