# Generated by Django 5.0.6 on 2024-05-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("image", models.FileField(upload_to="products/")),
                ("price", models.DecimalField(decimal_places=3, max_digits=10)),
                ("description", models.TextField()),
                ("popularity", models.IntegerField()),
            ],
        ),
    ]
