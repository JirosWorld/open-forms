# Generated by Django 3.2.18 on 2023-05-10 13:17

from django.db import migrations


# Initially we thought the new cosign component would replace the old one,
# but actually they will both exist for a while
class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0078_form_suspension_allowed"),
    ]

    operations = []
