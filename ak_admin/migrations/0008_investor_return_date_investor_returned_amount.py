# Generated by Django 4.2 on 2024-06-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ak_admin', '0007_investor_base_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='returned_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]