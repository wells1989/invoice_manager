# Generated by Django 5.0.4 on 2024-05-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "invoice",
            "0007_client_freelancer_history_invoice_invoice_been_paid_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="currency",
            field=models.CharField(default="EUR", max_length=3),
        ),
    ]
