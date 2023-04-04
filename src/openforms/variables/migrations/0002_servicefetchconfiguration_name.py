# Generated by Django 3.2.18 on 2023-03-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("variables", "0001_add_service_fetch_configuration"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicefetchconfiguration",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="human readable name for the configuration",
                max_length=250,
            ),
        ),
    ]
