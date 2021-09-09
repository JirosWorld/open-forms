# Generated by Django 2.2.24 on 2021-09-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointmentinfo",
            name="appointment_id",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="appointment ID"
            ),
        ),
        migrations.AlterField(
            model_name="appointmentsconfig",
            name="config_path",
            field=models.CharField(
                blank=True,
                choices=[
                    ("openforms.appointments.contrib.jcc.models.JccConfig", "Jcc"),
                    (
                        "openforms.appointments.contrib.qmatic.models.QmaticConfig",
                        "Qmatic",
                    ),
                ],
                max_length=255,
                verbose_name="appointment plugin",
            ),
        ),
    ]