from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class RegisterTestCase(APITestCase):
    def test_register_user(self):
        # Prepare the data for a new user registration
        data = {
            "username": "testuser", 
            "password": "testpassword", 
            "password2": "testpassword"  # Assuming this field is for password confirmation
        }
        # Send a POST request to the user registration endpoint
        response = self.client.post(reverse('auth_register'), data)
        # Assert that the response status code is 201 (HTTP Created),
        # indicating successful registration
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TokenObtainTestCase(APITestCase):
    def test_token_obtain(self):
        # Create a test user in the database
        User.objects.create_user(username='testuser', password='testpassword')
        # Prepare the data for obtaining a token
        data = {"username": "testuser", "password": "testpassword"}
        # Send a POST request to the token obtain endpoint
        response = self.client.post(reverse('token_obtain_pair'), data)
        # Assert that the response status code is 200 (HTTP OK),
        # indicating successful token retrieval
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the response data includes an 'access' key,
        # which typically holds the access token
        self.assertIn('access', response.data)
