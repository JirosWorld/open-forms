# Generated by Django 3.2.19 on 2023-06-15 13:07

import functools

from django.db import migrations

import tinymce.models

import openforms.config.models
import openforms.config.models.config
import openforms.emails.validators
import openforms.template.validators


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0048_add_cosign_templatetag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="globalconfiguration",
            name="confirmation_email_content",
            field=tinymce.models.HTMLField(
                default=functools.partial(
                    openforms.config.models.config._render,
                    *("emails/confirmation/content.html",),
                    **{}
                ),
                help_text="Content of the confirmation email message. Can be overridden on the form level",
                validators=[
                    openforms.template.validators.DjangoTemplateValidator(
                        backend="openforms.template.openforms_backend",
                        required_template_tags=[
                            "appointment_information",
                            "payment_information",
                            "cosign_information",
                        ],
                    ),
                    openforms.emails.validators.URLSanitationValidator(),
                ],
                verbose_name="content",
            ),
        ),
        migrations.AlterField(
            model_name="globalconfiguration",
            name="confirmation_email_content_en",
            field=tinymce.models.HTMLField(
                default=functools.partial(
                    openforms.config.models.config._render,
                    *("emails/confirmation/content.html",),
                    **{}
                ),
                help_text="Content of the confirmation email message. Can be overridden on the form level",
                null=True,
                validators=[
                    openforms.template.validators.DjangoTemplateValidator(
                        backend="openforms.template.openforms_backend",
                        required_template_tags=[
                            "appointment_information",
                            "payment_information",
                            "cosign_information",
                        ],
                    ),
                    openforms.emails.validators.URLSanitationValidator(),
                ],
                verbose_name="content",
            ),
        ),
        migrations.AlterField(
            model_name="globalconfiguration",
            name="confirmation_email_content_nl",
            field=tinymce.models.HTMLField(
                default=functools.partial(
                    openforms.config.models.config._render,
                    *("emails/confirmation/content.html",),
                    **{}
                ),
                help_text="Content of the confirmation email message. Can be overridden on the form level",
                null=True,
                validators=[
                    openforms.template.validators.DjangoTemplateValidator(
                        backend="openforms.template.openforms_backend",
                        required_template_tags=[
                            "appointment_information",
                            "payment_information",
                            "cosign_information",
                        ],
                    ),
                    openforms.emails.validators.URLSanitationValidator(),
                ],
                verbose_name="content",
            ),
        ),
    ]
