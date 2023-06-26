from rest_framework import serializers
from credit_card.models import CreditCard
from datetime import date, datetime
import calendar


class CreditCardSerializer(serializers.ModelSerializer):

    exp_date = serializers.DateField(input_formats=['%Y-%m-%d',])

    class Meta:
        model = CreditCard
        fields = ['id', 'holder', 'number', 'exp_date', 'cvv']

    def to_internal_value(self, data):
        # Convert exp_date from MM/YYYY to YYYY-MM-DD
        if 'exp_date' in data:
            try:
                month, year = map(int, data['exp_date'].split('/'))
                if not (1 <= month <= 12 and 1900 < year < 10000):
                    raise ValueError
            except ValueError:
                raise serializers.ValidationError("exp_date must be in 'MM/YYYY' format")

            last_day = calendar.monthrange(year, month)[1]  # Get the last day of the month
            data['exp_date'] = date(year, month, last_day)

        return super().to_internal_value(data)
        
    def create(self, validated_data):
        exp_date = validated_data['exp_date']
        if isinstance(exp_date, str):
            # Converte exp_date de MM/YYYY para um objeto date
            month, year = map(int, exp_date.split('/'))
            last_day = calendar.monthrange(year, month)[1]  # Obtem o último dia do mês
            validated_data['exp_date'] = date(year, month, last_day)  # Use date em vez de datetime

        return super().create(validated_data)

