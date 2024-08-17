# Generated by Django 4.2.3 on 2024-08-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_userprofile_profile_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Expertise",
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
                (
                    "start_date",
                    models.DateField(help_text="The start date of the expertise."),
                ),
                (
                    "end_date",
                    models.DateField(help_text="The end date of the expertise."),
                ),
                (
                    "position",
                    models.CharField(
                        help_text="The position held during the expertise.",
                        max_length=200,
                    ),
                ),
                (
                    "short_description",
                    models.TextField(
                        help_text="A brief description of the expertise.",
                        max_length=500,
                    ),
                ),
                (
                    "tools_and_technology",
                    models.CharField(
                        help_text="Tools and technologies used during the expertise.",
                        max_length=500,
                    ),
                ),
            ],
        ),
    ]
