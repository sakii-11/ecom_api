# Generated by Django 5.0.6 on 2024-05-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(),
        ),
    ]
