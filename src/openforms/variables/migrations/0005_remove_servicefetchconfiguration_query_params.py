# Generated by Django 3.2.18 on 2023-03-13 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("variables", "0004_migrate_query_params"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servicefetchconfiguration",
            name="query_params",
        ),
    ]
