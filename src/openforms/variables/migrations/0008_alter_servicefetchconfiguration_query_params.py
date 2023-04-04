# Generated by Django 3.2.18 on 2023-03-27 07:51

from django.db import migrations, models

import openforms.variables.validators


class Migration(migrations.Migration):

    dependencies = [
        ("variables", "0007_alter_servicefetchconfiguration_headers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicefetchconfiguration",
            name="query_params",
            field=models.JSONField(
                blank=True,
                default=dict,
                validators=[openforms.variables.validators.QueryParameterValidator()],
                verbose_name="HTTP query string",
            ),
        ),
    ]
