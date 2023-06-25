from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class TestToken(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='testpassword')
        self.url = reverse('token_obtain_pair')

    def test_token_obtain(self):
        response = self.client.post(self.url, {'username': 'test', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)

    def test_invalid_credentials(self):
        response = self.client.post(self.url, {'username': 'invalid', 'password': 'invalid'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse('access' in response.data)


class TestTokenRefresh(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='testpassword')
        self.url_obtain_token = reverse('token_obtain_pair')
        response = self.client.post(self.url_obtain_token, {'username': 'test', 'password': 'testpassword'}, format='json')
        self.refresh_token = response.data['refresh']
        self.url_refresh_token = reverse('token_refresh')

    def test_token_refresh(self):
        response = self.client.post(self.url_refresh_token, {'refresh': self.refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)

    def test_invalid_refresh_token(self):
        response = self.client.post(self.url_refresh_token, {'refresh': 'invalidrefresh'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse('access' in response.data)
