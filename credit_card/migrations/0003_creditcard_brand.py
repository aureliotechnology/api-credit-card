# Generated by Django 4.2.2 on 2023-06-26 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_card', '0002_alter_creditcard_exp_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='brand',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
