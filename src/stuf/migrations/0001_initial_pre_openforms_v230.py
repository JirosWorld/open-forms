# Generated by Django 3.2.20 on 2023-09-11 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("stuf", "0001_initial"),
        ("stuf", "0002_auto_20210527_1125"),
        ("stuf", "0003_auto_20210604_1355"),
        ("stuf", "0004_auto_20210722_1826"),
        ("stuf", "0005_auto_20210722_1827"),
        ("stuf", "0006_auto_20210722_1832"),
        ("stuf", "0007_auto_20210924_1518"),
        ("stuf", "0008_auto_20210927_1555"),
        ("stuf", "0009_auto_20220404_1050"),
        ("stuf", "0010_auto_20220404_1053"),
        ("stuf", "0011_auto_20220404_1119"),
        ("stuf", "0012_auto_20220905_2218"),
    ]

    dependencies = [
        ("soap", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StufService",
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
                    "ontvanger_organisatie",
                    models.CharField(
                        blank=True,
                        help_text="Field 'ontvanger organisatie' in StUF",
                        max_length=200,
                        verbose_name="receiving organisation",
                    ),
                ),
                (
                    "ontvanger_applicatie",
                    models.CharField(
                        help_text="Field 'ontvanger applicatie' in StUF",
                        max_length=200,
                        verbose_name="receiving application",
                    ),
                ),
                (
                    "ontvanger_administratie",
                    models.CharField(
                        blank=True,
                        help_text="Field 'ontvanger administratie' in StUF",
                        max_length=200,
                        verbose_name="receiving administration",
                    ),
                ),
                (
                    "ontvanger_gebruiker",
                    models.CharField(
                        blank=True,
                        help_text="Field 'ontvanger gebruiker' in StUF",
                        max_length=200,
                        verbose_name="receiving user",
                    ),
                ),
                (
                    "zender_organisatie",
                    models.CharField(
                        blank=True,
                        help_text="Field 'zender organisatie' in StUF",
                        max_length=200,
                        verbose_name="sending organisation",
                    ),
                ),
                (
                    "zender_applicatie",
                    models.CharField(
                        help_text="Field 'zender applicatie' in StUF",
                        max_length=200,
                        verbose_name="sending application",
                    ),
                ),
                (
                    "zender_administratie",
                    models.CharField(
                        blank=True,
                        help_text="Field 'zender administratie' in StUF",
                        max_length=200,
                        verbose_name="sending administration",
                    ),
                ),
                (
                    "zender_gebruiker",
                    models.CharField(
                        blank=True,
                        help_text="Field 'zender gebruiker' in StUF",
                        max_length=200,
                        verbose_name="sending user",
                    ),
                ),
                (
                    "endpoint_beantwoord_vraag",
                    models.URLField(
                        blank=True,
                        help_text="Endpoint for synchronous request messages, usually '[...]/BeantwoordVraag'",
                        verbose_name="endpoint BeantwoordVraag",
                    ),
                ),
                (
                    "endpoint_vrije_berichten",
                    models.URLField(
                        blank=True,
                        help_text="Endpoint for synchronous free messages, usually '[...]/VerwerkSynchroonVrijBericht' or '[...]/VrijeBerichten'.",
                        verbose_name="endpoint VrijeBerichten",
                    ),
                ),
                (
                    "endpoint_ontvang_asynchroon",
                    models.URLField(
                        blank=True,
                        help_text="Endpoint for asynchronous messages, usually '[...]/OntvangAsynchroon'.",
                        verbose_name="endpoint OntvangAsynchroon",
                    ),
                ),
                (
                    "soap_service",
                    models.OneToOneField(
                        help_text="The soap service this stuf service uses",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuf_service",
                        to="soap.soapservice",
                    ),
                ),
            ],
            options={
                "verbose_name": "StUF service",
                "verbose_name_plural": "StUF services",
            },
        ),
    ]
