# Generated by Django 4.1.3 on 2022-11-20 04:18

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0002_pracownicy_produkt_zamowienia_delete_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]