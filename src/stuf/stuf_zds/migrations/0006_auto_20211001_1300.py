# Generated by Django 2.2.24 on 2021-10-01 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stuf", "0008_auto_20210927_1555"),
        ("stuf_zds", "0005_stufzdsconfig_zds_zaaktype_status_omschrijving"),
    ]

    operations = [
        migrations.RenameField(
            model_name="stufzdsconfig",
            old_name="service",
            new_name="old_service",
        ),
        migrations.AddField(
            model_name="stufzdsconfig",
            name="new_service",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="stuf_zds_config",
                to="stuf.StufService",
            ),
        ),
        # there used to be a data migration here, but it's guaranteed to have been
        # executed if you're on 2.3.0+
        migrations.RenameField(
            model_name="stufzdsconfig",
            old_name="new_service",
            new_name="service",
        ),
        migrations.RemoveField(
            model_name="stufzdsconfig",
            name="old_service",
        ),
    ]
