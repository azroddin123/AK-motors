# Generated by Django 5.0.6 on 2024-07-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("username", models.CharField(max_length=50)),
                (
                    "profile_pic",
                    models.ImageField(blank=True, null=True, upload_to="user/"),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[("Admin", "Admin"), ("Employee", "Employee")],
                        default="Employee",
                        max_length=250,
                    ),
                ),
                ("accepted_policy", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
