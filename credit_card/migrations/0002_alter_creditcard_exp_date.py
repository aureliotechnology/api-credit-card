# Generated by Django 4.2.2 on 2023-06-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='exp_date',
            field=models.DateField(),
        ),
    ]
