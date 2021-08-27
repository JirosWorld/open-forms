# Generated by Django 2.2.24 on 2021-08-24 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("zgw_consumers", "0012_auto_20210104_1039"),
    ]

    operations = [
        migrations.CreateModel(
            name="QmaticConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "service",
                    models.OneToOneField(
                        help_text="The Qmatic Orchestra Calendar Public Appointment API service. Example: https://example.com:8443/calendar-backend/public/api/v1/",
                        limit_choices_to={"api_type": "orc"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="zgw_consumers.Service",
                        verbose_name="Calendar API",
                    ),
                ),
            ],
            options={
                "verbose_name": "Qmatic configuration",
            },
        ),
    ]