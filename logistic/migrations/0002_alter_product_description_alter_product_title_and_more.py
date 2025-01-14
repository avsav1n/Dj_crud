# Generated by Django 5.1.2 on 2024-10-19 13:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='address',
            field=models.CharField(max_length=200, unique=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=18, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AddConstraint(
            model_name='stockproduct',
            constraint=models.UniqueConstraint(fields=('stock', 'product'), name='stock-product-unique-constraint'),
        ),
    ]
