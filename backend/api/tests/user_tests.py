from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class RegisterTestCase(APITestCase):
    def test_register_user(self):
        """
        新規ユーザー登録のテスト
        """
        data = {"username": "testuser", "password": "testpassword", "password2": "testpassword"}
        response = self.client.post(reverse('auth_register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TokenObtainTestCase(APITestCase):
    def test_token_obtain(self):
        """
        トークン取得のテスト
        """
        User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('token_obtain_pair'), {"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)