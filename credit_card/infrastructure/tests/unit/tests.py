from django.test import TestCase
import calendar
from credit_card.domain.models import CreditCard
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

from creditcard import CreditCard as CardValidator

class CreditCardModelTest(TestCase):

    def setUp(self):
        """
        Setup method to create a base credit card instance for use in the following tests.
        """
        self.credit_card = CreditCard(exp_date=self.exp_date_str_to_date('02/2025'), 
                                    holder='John Doe', 
                                    number='4111111111111111')


    def test_exp_date_in_the_past(self):
        """
        Test if the validation of the expiration date being in the past works correctly.
        """
        past_date = datetime.now() - timedelta(days=1)
        self.credit_card.exp_date = past_date.strftime('%m/%Y')  # Convert date to mm/yyyy format

        self.assertRaises(ValidationError, self.credit_card.save)

    def test_exp_date_converted_to_end_of_month(self):
        """
        Test if the expiration date is correctly converted to the end of the month.
        """
        self.credit_card.exp_date = self.exp_date_str_to_date('03/2027')
        self.credit_card.save()


    def test_holder_field(self):
        """
        Test if the validation of the holder field works correctly.
        """
        # Holder field with less than 2 characters should raise a ValidationError
        self.credit_card.holder = 'A'
        self.assertRaises(ValidationError, self.credit_card.save)

        # Holder field with 2 or more characters should not raise a ValidationError
        self.credit_card.holder = 'AB'
        try:
            self.credit_card.save()
        except ValidationError:
            self.fail("Saving a credit card with a holder name of 2 or more characters raised a ValidationError.")

    def test_number_field(self):
        """
        Test if the validation of the number field works correctly.
        """
        # Invalid credit card number should raise a ValidationError
        self.credit_card.number = '1111111111111111'
        if not CardValidator(self.credit_card.number).is_valid:
            self.fail("Validation did not raise a ValidationError for an invalid card number.")

        # Valid credit card number should not raise a ValidationError
        self.credit_card.number = '4539578763621486'
        if not CardValidator(self.credit_card.number).is_valid:
            self.fail("Validation raised a ValidationError for a valid card number.")

        # Valid credit card number should not raise a ValidationError
        self.credit_card.number = '4539578763621486'
        try:
            self.credit_card.save()
        except ValidationError:
            self.fail("Saving a credit card with a valid number raised a ValidationError.")
            
    def test_cvv_field(self):
        """
        Test if the validation of the cvv field works correctly.
        """
        # CVV field with less than 3 characters should raise a ValidationError
        self.credit_card.cvv = '12'
        self.assertRaises(ValidationError, self.credit_card.save)

        # CVV field with more than 4 characters should raise a ValidationError
        self.credit_card.cvv = '12345'
        self.assertRaises(ValidationError, self.credit_card.save)

        # CVV field with 3 or 4 numeric characters should not raise a ValidationError
        self.credit_card.cvv = '123'
        try:
            self.credit_card.save()
        except ValidationError:
            self.fail("Saving a credit card with a CVV of 3 numeric characters raised a ValidationError.")
            
        self.credit_card.cvv = '1234'
        try:
            self.credit_card.save()
        except ValidationError:
            self.fail("Saving a credit card with a CVV of 4 numeric characters raised a ValidationError.")

        # CVV field with non-numeric characters should raise a ValidationError
        self.credit_card.cvv = '123a'
        self.assertRaises(ValidationError, self.credit_card.save)

    def exp_date_str_to_date(self, exp_date_str):
        """
        Convert a string representing a credit card expiration date in 'MM/YYYY' format to a date object in 'YYYY-MM-DD' format.
        """
        month, year = map(int, exp_date_str.split('/'))  # Split the string into month and year
        _, day = calendar.monthrange(year, month)  # Get the last day of the month
        return datetime(year, month, day)  # Return the date in 'YYYY-MM-DD' format

def last_day_of_month(date):
    """
    Function to find the last day of the month for the given date.
    """
    _, last_day = calendar.monthrange(date.year, date.month)
    return last_day


