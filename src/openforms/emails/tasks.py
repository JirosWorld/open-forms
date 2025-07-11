from datetime import datetime, timedelta
from typing import Any

from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from openforms.celery import app
from openforms.config.models import GlobalConfiguration

from .digest import (
    collect_broken_configurations,
    collect_expired_or_near_expiry_reference_lists_data,
    collect_failed_emails,
    collect_failed_prefill_plugins,
    collect_failed_registrations,
    collect_invalid_certificates,
    collect_invalid_logic_rules,
    collect_invalid_registration_backends,
)
from .utils import send_mail_html


class Digest:
    def __init__(self, since: datetime) -> None:
        self.since = since

    def get_context_data(self) -> dict[str, Any]:
        failed_emails = collect_failed_emails(self.since)
        failed_registrations = collect_failed_registrations(self.since)
        failed_prefill_plugins = collect_failed_prefill_plugins(self.since)
        broken_configurations = collect_broken_configurations()
        invalid_certificates = collect_invalid_certificates()
        invalid_registration_backends = collect_invalid_registration_backends()
        invalid_logic_rules = collect_invalid_logic_rules()
        expired_or_near_expiry_reference_lists_data = (
            collect_expired_or_near_expiry_reference_lists_data()
        )

        return {
            "failed_emails": failed_emails,
            "failed_registrations": failed_registrations,
            "failed_prefill_plugins": failed_prefill_plugins,
            "broken_configurations": broken_configurations,
            "invalid_certificates": invalid_certificates,
            "invalid_registration_backends": invalid_registration_backends,
            "invalid_logic_rules": invalid_logic_rules,
            "expired_or_near_expiry_reference_lists_data": expired_or_near_expiry_reference_lists_data,
        }

    def render(self) -> str:
        context = self.get_context_data()
        if not any(context.values()):
            return ""

        return render_to_string("emails/admin_digest.html", context)


@app.task
def send_email_digest() -> None:
    config = GlobalConfiguration.get_solo()
    if not (recipients := config.recipients_email_digest):
        return

    yesterday = timezone.now() - timedelta(days=1)
    digest = Digest(since=yesterday)
    content = digest.render()

    if not content:
        return

    send_mail_html(
        _("[Open Forms] Daily summary of detected problems"),
        content,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
    )


@app.task()
def delete_old_emails(days=90):
    """
    Delete emails created before `days` days (default 90).

    Override for django_yubin.tasks.delete_old_emails which caused memory issues while
    using the DatabaseStorageBackend because the email data and attachments would be loaded.
    """

    from django_yubin.models import Message

    cutoff_date = timezone.now() - timedelta(days)
    deleted = (
        Message.objects.defer("_message_data")
        .filter(date_created__lt=cutoff_date)
        .delete()
    )

    return deleted, cutoff_date
