# Generated by Django 2.2.24 on 2021-09-03 10:42

import functools

import django.contrib.postgres.fields.jsonb
import django.core.validators
import django.db.migrations.operations.special
import django.db.models.deletion
from django.core.management import call_command
from django.db import migrations, models

import django_better_admin_arrayfield.models.fields
import tinymce.models

import openforms.utils.fields
import openforms.utils.translations


def load_cookiegroups(*args):
    call_command("loaddata", "cookie_consent")


class Migration(migrations.Migration):

    replaces = [
        ("config", "0001_initial"),
        ("config", "0002_auto_20210514_1034"),
        ("config", "0003_auto_20210514_1453"),
        ("config", "0004_auto_20210521_1352"),
        ("config", "0005_globalconfiguration_default_test_bsn"),
        ("config", "0006_auto_20210603_1524"),
        ("config", "0007_globalconfiguration_display_sdk_information"),
        ("config", "0005_globalconfiguration_enable_react_form"),
        ("config", "0008_merge_20210607_1043"),
        ("config", "0008_globalconfiguration_default_test_kvk"),
        ("config", "0009_merge_20210621_1635"),
        ("config", "0009_globalconfiguration_submission_confirmation_template"),
        ("config", "0010_merge_20210621_1740"),
        ("config", "0011_auto_20210624_1007"),
        ("config", "0012_globalconfiguration_allow_empty_initiator"),
        ("config", "0013_auto_20210715_1615"),
        ("config", "0014_auto_20210716_1046"),
        ("config", "0015_globalconfiguration_analytics_cookie_consent_group"),
        ("config", "0016_load_default_cookiegroups"),
        ("config", "0017_auto_20210726_0948"),
        ("config", "0017_auto_20210724_0801"),
        ("config", "0018_merge_20210726_1031"),
        ("config", "0019_auto_20210730_1446"),
        ("config", "0020_auto_20210730_1610"),
        ("config", "0021_globalconfiguration_enable_demo_plugins"),
        ("config", "0021_auto_20210823_0909"),
        ("config", "0022_merge_20210903_1228"),
    ]

    dependencies = [
        ("cookie_consent", "0002_auto__add_logitem"),
    ]

    operations = [
        migrations.RunPython(
            code=load_cookiegroups,
            reverse_code=migrations.operations.special.RunPython.noop,
        ),
        migrations.CreateModel(
            name="GlobalConfiguration",
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
                    "email_template_netloc_allowlist",
                    django_better_admin_arrayfield.models.fields.ArrayField(
                        base_field=models.CharField(max_length=1000),
                        blank=True,
                        default=list,
                        help_text="Provide a list of allowed domains (without 'https://www').Hyperlinks in a (confirmation) email are removed, unless the domain is provided here.",
                        size=None,
                        verbose_name="allowed email domain names",
                    ),
                ),
                (
                    "default_test_bsn",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="When provided, submissions that are started will have this BSN set as default for the session. Useful to test/demo prefill functionality.",
                        max_length=9,
                        verbose_name="default test BSN",
                    ),
                ),
                (
                    "display_sdk_information",
                    models.BooleanField(
                        default=False,
                        help_text="When enabled, information about the used SDK is displayed.",
                        verbose_name="display SDK information",
                    ),
                ),
                (
                    "enable_react_form",
                    models.BooleanField(
                        default=False,
                        help_text="If enabled, the admin page to create forms will use the new React page.",
                        verbose_name="enable React form page",
                    ),
                ),
                (
                    "default_test_kvk",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="When provided, submissions that are started will have this KvK Number set as default for the session. Useful to test/demo prefill functionality.",
                        max_length=9,
                        verbose_name="default test KvK Number",
                    ),
                ),
                (
                    "submission_confirmation_template",
                    tinymce.models.HTMLField(
                        default="Thank you for submitting this form.",
                        help_text="The content of the submission confirmation page. It can contain variables that will be templated from the submitted form data.",
                        verbose_name="submission confirmation template",
                    ),
                ),
                (
                    "allow_empty_initiator",
                    models.BooleanField(
                        default=False,
                        help_text="When enabled and the submitter is not authenticated, a case is created without any initiator. Otherwise, a fake initiator is added with BSN 111222333.",
                        verbose_name="allow empty initiator",
                    ),
                ),
                (
                    "form_begin_text",
                    models.CharField(
                        default=functools.partial(
                            openforms.utils.translations.get_default,
                            *("Begin form",),
                            **{}
                        ),
                        help_text="The text that will be displayed at the start of the form to indicate the user can begin to fill in the form",
                        max_length=50,
                        verbose_name="begin text",
                    ),
                ),
                (
                    "form_change_text",
                    models.CharField(
                        default=functools.partial(
                            openforms.utils.translations.get_default, *("Change",), **{}
                        ),
                        help_text="The text that will be displayed in the overview page to change a certain step",
                        max_length=50,
                        verbose_name="change text",
                    ),
                ),
                (
                    "form_confirm_text",
                    models.CharField(
                        default=functools.partial(
                            openforms.utils.translations.get_default,
                            *("Confirm",),
                            **{}
                        ),
                        help_text="The text that will be displayed in the overview page to confirm the form is filled in correctly",
                        max_length=50,
                        verbose_name="confirm text",
                    ),
                ),
                (
                    "form_previous_text",
                    models.CharField(
                        default=functools.partial(
                            openforms.utils.translations.get_default,
                            *("Previous page",),
                            **{}
                        ),
                        help_text="The text that will be displayed in the overview page to go to the previous step",
                        max_length=50,
                        verbose_name="previous text",
                    ),
                ),
                (
                    "form_step_next_text",
                    models.CharField(
                        default=functools.partial(
                            openforms.utils.translations.get_default, *("Next",), **{}
                        ),
                        help_text="The text that will be displayed in the form step to go to the next step",
                        max_length=50,
                        verbose_name="step next text",
                    ),
                ),
                (
                    "form_step_previous_text",
                    models.CharField(
                        default=functools.partial(
                            openforms.utils.translations.get_default,
                            *("Previous page",),
                            **{}
                        ),
                        help_text="The text that will be displayed in the form step to go to the previous step",
                        max_length=50,
                        verbose_name="step previous text",
                    ),
                ),
                (
                    "form_step_save_text",
                    models.CharField(
                        default=functools.partial(
                            openforms.utils.translations.get_default,
                            *("Save current information",),
                            **{}
                        ),
                        help_text="The text that will be displayed in the form step to save the current information",
                        max_length=50,
                        verbose_name="step save text",
                    ),
                ),
                (
                    "ga_code",
                    models.CharField(
                        blank=True,
                        help_text="Typically looks like 'UA-XXXXX-Y'. Supplying this installs Google Analytics.",
                        max_length=50,
                        verbose_name="Google Analytics code",
                    ),
                ),
                (
                    "gtm_code",
                    models.CharField(
                        blank=True,
                        help_text="Typically looks like 'GTM-XXXX'. Supplying this installs Google Tag Manager.",
                        max_length=50,
                        verbose_name="Google Tag Manager code",
                    ),
                ),
                (
                    "matomo_site_id",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="The 'idsite' of the website you're tracking in Matomo.",
                        null=True,
                        verbose_name="Matomo site ID",
                    ),
                ),
                (
                    "matomo_url",
                    models.CharField(
                        blank=True,
                        help_text="The base URL of your Matomo server, e.g. 'matomo.example.com'.",
                        max_length=255,
                        verbose_name="Matomo server URL",
                    ),
                ),
                (
                    "piwik_site_id",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="The 'idsite' of the website you're tracking in Piwik.",
                        null=True,
                        verbose_name="Piwik site ID",
                    ),
                ),
                (
                    "piwik_url",
                    models.CharField(
                        blank=True,
                        help_text="The base URL of your Piwik server, e.g. 'piwik.example.com'.",
                        max_length=255,
                        verbose_name="Piwik server URL",
                    ),
                ),
                (
                    "siteimprove_id",
                    models.CharField(
                        blank=True,
                        help_text="Your SiteImprove ID - you can find this from the embed snippet example, which should contain a URL like '//siteimproveanalytics.com/js/siteanalyze_XXXXX.js'. The XXXXX is your ID.",
                        max_length=10,
                        verbose_name="SiteImprove ID",
                    ),
                ),
                (
                    "analytics_cookie_consent_group",
                    models.ForeignKey(
                        blank=True,
                        help_text="The cookie group used for analytical cookies. The analytics scripts are loaded only if this cookie group is accepted by the end-user.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cookie_consent.CookieGroup",
                    ),
                ),
                (
                    "admin_session_timeout",
                    models.PositiveIntegerField(
                        default=60,
                        help_text="Amount of time in minutes the admin can be inactive for before being logged out",
                        validators=[django.core.validators.MinValueValidator(5)],
                        verbose_name="admin session timeout",
                    ),
                ),
                (
                    "form_session_timeout",
                    models.PositiveIntegerField(
                        default=60,
                        help_text="Amount of time in minutes a user filling in a form can be inactive for before being logged out",
                        validators=[django.core.validators.MinValueValidator(5)],
                        verbose_name="form session timeout",
                    ),
                ),
                (
                    "design_token_values",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Values of various style parameters, such as border radii, background colors... Note that this is advanced usage. Any available but un-specified values will use fallback default values.",
                        verbose_name="design token values",
                    ),
                ),
                (
                    "main_website",
                    models.URLField(
                        blank=True,
                        help_text="URL to the main website. Used for the 'back to municipality website' link.",
                        verbose_name="main website link",
                    ),
                ),
                (
                    "logo",
                    openforms.utils.fields.SVGOrImageField(
                        blank=True,
                        help_text="Upload the municipality logo, visible to users filling out forms. We advise dimensions around 150px by 75px. SVG's are allowed.",
                        upload_to="logo/",
                        verbose_name="municipality logo",
                    ),
                ),
                (
                    "enable_demo_plugins",
                    models.BooleanField(
                        default=False,
                        help_text="If enabled, the admin allows selection of demo backend plugins.",
                        verbose_name="enable demo plugins",
                    ),
                ),
                (
                    "all_submissions_removal_limit",
                    models.PositiveIntegerField(
                        default=90,
                        help_text="Amount of days when all submissions will be permanently deleted",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="all submissions removal limit",
                    ),
                ),
                (
                    "errored_submissions_removal_limit",
                    models.PositiveIntegerField(
                        default=30,
                        help_text="Amount of days errored submissions will remain before being removed",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="errored submission removal limit",
                    ),
                ),
                (
                    "errored_submissions_removal_method",
                    models.CharField(
                        choices=[
                            ("delete_permanently", "Submissions will be deleted"),
                            (
                                "make_anonymous",
                                "Sensitive data within the submissions will be deleted",
                            ),
                        ],
                        default="delete_permanently",
                        help_text="How errored submissions will be removed after the",
                        max_length=50,
                        verbose_name="errored submissions removal method",
                    ),
                ),
                (
                    "incomplete_submissions_removal_limit",
                    models.PositiveIntegerField(
                        default=7,
                        help_text="Amount of days incomplete submissions will remain before being removed",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="incomplete submission removal limit",
                    ),
                ),
                (
                    "incomplete_submissions_removal_method",
                    models.CharField(
                        choices=[
                            ("delete_permanently", "Submissions will be deleted"),
                            (
                                "make_anonymous",
                                "Sensitive data within the submissions will be deleted",
                            ),
                        ],
                        default="delete_permanently",
                        help_text="How incomplete submissions will be removed after the limit",
                        max_length=50,
                        verbose_name="incomplete submissions removal method",
                    ),
                ),
                (
                    "successful_submissions_removal_limit",
                    models.PositiveIntegerField(
                        default=7,
                        help_text="Amount of days successful submissions will remain before being removed",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="successful submission removal limit",
                    ),
                ),
                (
                    "successful_submissions_removal_method",
                    models.CharField(
                        choices=[
                            ("delete_permanently", "Submissions will be deleted"),
                            (
                                "make_anonymous",
                                "Sensitive data within the submissions will be deleted",
                            ),
                        ],
                        default="delete_permanently",
                        help_text="How successful submissions will be removed after the limit",
                        max_length=50,
                        verbose_name="successful submissions removal method",
                    ),
                ),
            ],
            options={
                "verbose_name": "General configuration",
            },
        ),
    ]
