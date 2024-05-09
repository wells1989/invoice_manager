# Generated by Django 5.0.4 on 2024-05-02 10:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Freelancer",
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
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=300)),
                (
                    "email",
                    models.CharField(
                        max_length=100,
                        validators=[django.core.validators.EmailValidator()],
                    ),
                ),
                (
                    "contact",
                    models.IntegerField(
                        validators=[django.core.validators.MinLengthValidator(6)]
                    ),
                ),
            ],
        ),
    ]