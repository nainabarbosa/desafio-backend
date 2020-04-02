import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Trip
from django.contrib.auth.models import User
from .serializers import TripsSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    def make_request(self, kind="put", **kwargs):
        """
        Make a put request to update a trip
        :param kind: HTTP VERB
        :return:
        """        
        if kind == "put":
            return self.client.put(
                reverse(
                    "trip-update",
                    kwargs={
                        "pk": kwargs["id"]
                    }
                ),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )
        else:
            return None

    def user_login(self, username="", password=""):
        url = reverse(
            "auth-login"
        )
        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type="application/json"
        )

    def setUp(self):

        # create a admin user
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )

        self.valid_data = {'id': 2, 'category': 1, 'nota': 5}

        
class GetAllTripsTest(BaseViewTest):

    def test_get_all_trips(self):
        """
        This test ensures that all trips added in the setUp method
        exist when we make a GET request to the trips/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("trips-list")
        )
        # fetch the data from db
        trips_data = Trip.objects.all()
        serialized = TripsSerializer(trips_data, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class UpdateTripsTest(BaseViewTest):

#     def test_update_trip(self):
#         """
#         This test ensures that a trip can be updated.
#         """

#         # hit the API endpoint
#         response = self.make_request(
#             kind="put",
#             version="v1",
#             id=2,
#             data=self.valid_data
#         )
#         self.assertEqual(response.data, self.valid_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


class AuthLoginUserTest(BaseViewTest):
    """
    Tests for the auth/login/ endpoint
    """

    def test_login_user_with_valid_credentials(self):
        # test login with valid credentials
        response = self.user_login("test_user", "testing")
        # assert token key exists
        self.assertIn("token", response.data)
        # assert status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)