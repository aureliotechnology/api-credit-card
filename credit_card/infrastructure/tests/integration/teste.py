import calendar
from datetime import datetime
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken 


class CreditCardAPITests(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        # URL for creating a credit card
        self.create_credit_card_url = reverse('creditcard-list')

        # Define a valid payload with a dynamic expiration date
        next_year = datetime.now().year + 1  # Get next year
        current_month = datetime.now().month  # Get current month
        exp_date = f'{current_month}/{next_year}'  # Format as 'MM/YYYY'

        self.valid_payload = {
            'holder': 'John Doe',
            'number': '4111111111111111',  # Visa test number
            'exp_date': exp_date,
            'cvv': '123'
        }

    def test_create_credit_card(self):
        """
        Ensure we can create a new credit card.
        """
        response = self.client.post(self.create_credit_card_url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        month, year = map(int, self.valid_payload['exp_date'].split('/'))
        last_day = calendar.monthrange(year, month)[1]  
        converted_date = f'{year}-{month:02d}-{last_day}'

        for field in self.valid_payload:
            if field == 'exp_date':
                self.assertEqual(response.data[field], converted_date)
            elif field == 'cvv':
                self.assertEqual(response.data[field], int(self.valid_payload[field]))
            else:
                self.assertEqual(response.data[field], self.valid_payload[field])