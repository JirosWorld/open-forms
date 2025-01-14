# Generated by Django 3.2.21 on 2023-10-24 14:35

import django.db.models.deletion
from django.db import migrations, models

import openforms.variables.validators


class Migration(migrations.Migration):

    replaces = [
        ("variables", "0001_add_service_fetch_configuration"),
        ("variables", "0002_servicefetchconfiguration_name"),
        ("variables", "0003_servicefetchconfiguration__query_params"),
        ("variables", "0004_migrate_query_params"),
        ("variables", "0005_remove_servicefetchconfiguration_query_params"),
        (
            "variables",
            "0006_rename__query_params_servicefetchconfiguration_query_params",
        ),
        ("variables", "0007_alter_servicefetchconfiguration_headers"),
        ("variables", "0008_alter_servicefetchconfiguration_query_params"),
        ("variables", "0009_servicefetchconfiguration_name"),
        ("variables", "0010_alter_servicefetchconfiguration_name"),
        ("variables", "0011_migrate_interpolation_format"),
    ]

    dependencies = [
        ("zgw_consumers", "0016_auto_20220818_1412"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceFetchConfiguration",
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
                    "path",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="path relative to the Service API root",
                        max_length=250,
                        verbose_name="path",
                    ),
                ),
                (
                    "method",
                    models.CharField(
                        choices=[("GET", "GET"), ("POST", "POST")],
                        default="GET",
                        help_text="POST is allowed, but should not be used to mutate data",
                        max_length=4,
                        verbose_name="HTTP method",
                    ),
                ),
                (
                    "headers",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Additions and overrides for the HTTP request headers as defined in the Service.",
                        validators=[openforms.variables.validators.HeaderValidator()],
                        verbose_name="HTTP request headers",
                    ),
                ),
                (
                    "body",
                    models.JSONField(
                        blank=True,
                        help_text='Request body for POST requests (only "application/json" is supported)',
                        null=True,
                        verbose_name="HTTP request body",
                    ),
                ),
                (
                    "data_mapping_type",
                    models.CharField(
                        blank=True,
                        choices=[("JsonLogic", "JsonLogic"), ("jq", "jq")],
                        default="",
                        max_length=10,
                        verbose_name="mapping expression language",
                    ),
                ),
                (
                    "mapping_expression",
                    models.JSONField(
                        blank=True,
                        help_text="For jq, pass a string containing the filter expression",
                        null=True,
                        verbose_name="mapping expression",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="zgw_consumers.service",
                        verbose_name="service",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="human readable name for the configuration",
                        max_length=250,
                    ),
                ),
                (
                    "query_params",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        validators=[
                            openforms.variables.validators.QueryParameterValidator()
                        ],
                        verbose_name="HTTP query string",
                    ),
                ),
            ],
            options={
                "verbose_name": "service fetch configuration",
                "verbose_name_plural": "service fetch configurations",
            },
        ),
    ]
