# Generated by Django 4.2 on 2024-06-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ak_admin', '0006_auto_20240525_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='base_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]