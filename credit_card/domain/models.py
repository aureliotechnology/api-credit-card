from django.db import models
from django.core.exceptions import ValidationError
from creditcard import CreditCard as CardValidator
from datetime import datetime, date
from calendar import monthrange


class CreditCard(models.Model):
    holder = models.CharField(max_length=255)
    number = models.CharField(max_length=19)
    exp_date = models.DateField()
    cvv = models.IntegerField(blank=True, null=True)

    def _validate_holder(self):
        if len(self.holder) < 2:
            raise ValidationError('Card holder name must be at least 2 characters long.')

    def _validate_number(self):
        if not CardValidator(self.number).is_valid:
            raise ValidationError('Invalid card number.')

    def _validate_exp_date(self):
        # Convert the exp_date from mm/yyyy to a datetime object
        if isinstance(self.exp_date, str):
            month, year = map(int, self.exp_date.split('/'))
        elif isinstance(self.exp_date, date):  # Use date instead of datetime.date
            month = self.exp_date.month
            year = self.exp_date.year
        last_day_of_month = monthrange(year, month)[1]
        self.exp_date = datetime(year, month, last_day_of_month)

        if self.exp_date <= datetime.now():
            raise ValidationError('Card expiration date must be in the future.')

    def _validate_cvv(self):
        if self.cvv:
            cvv_str = str(self.cvv)
            if not (3 <= len(cvv_str) <= 4):
                raise ValidationError('CVV must be a 3 or 4 digit number.')

    def clean(self):
        self._validate_holder()
        self._validate_number()
        self._validate_exp_date()
        self._validate_cvv()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(CreditCard, self).save(*args, **kwargs)
