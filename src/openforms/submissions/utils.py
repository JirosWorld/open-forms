import logging
from typing import Any

from django.conf import settings
from django.contrib.sessions.backends.base import SessionBase

from openforms.appointments.service import get_confirmation_mail_suffix
from openforms.emails.confirmation_emails import (
    SkipConfirmationEmail,
    get_confirmation_email_context_data,
    get_confirmation_email_templates,
)
from openforms.emails.utils import (
    render_email_template,
    send_mail_html,
    strip_tags_plus,
)
from openforms.forms.constants import FormVariableSources
from openforms.forms.models import FormVariable
from openforms.logging import logevent

from .constants import SUBMISSIONS_SESSION_KEY, UPLOADS_SESSION_KEY
from .models import Submission, SubmissionValueVariable, TemporaryFileUpload
from .query import SubmissionQuerySet

logger = logging.getLogger(__name__)


def append_to_session_list(session: SessionBase, session_key: str, value: Any) -> None:
    # note: possible race condition with concurrent requests
    active = session.get(session_key, [])
    if value not in active:
        active.append(value)
        session[session_key] = active


def remove_from_session_list(
    session: SessionBase, session_key: str, value: Any
) -> None:
    # note: possible race condition with concurrent requests
    active = session.get(session_key, [])
    if value in active:
        active.remove(value)
        session[session_key] = active


def add_submmission_to_session(submission: Submission, session: SessionBase) -> None:
    """
    Store the submission UUID in the request session for authorization checks.
    """
    append_to_session_list(session, SUBMISSIONS_SESSION_KEY, str(submission.uuid))


def remove_submission_from_session(
    submission: Submission, session: SessionBase
) -> None:
    """
    Remove the submission UUID from the session if it's present.
    """
    remove_from_session_list(session, SUBMISSIONS_SESSION_KEY, str(submission.uuid))


def get_submissions_from_session(session: SessionBase) -> SubmissionQuerySet:
    """
    Retrieve the submission instances that are currently in the session.
    """
    uuids = session.get(SUBMISSIONS_SESSION_KEY, [])
    return Submission.objects.filter(uuid__in=uuids)


def add_upload_to_session(upload: TemporaryFileUpload, session: SessionBase) -> None:
    """
    Store the upload UUID in the request session for authorization checks.
    """
    append_to_session_list(session, UPLOADS_SESSION_KEY, str(upload.uuid))


def remove_upload_from_session(
    upload: TemporaryFileUpload, session: SessionBase
) -> None:
    """
    Remove the submission UUID from the session if it's present.
    """
    remove_from_session_list(session, UPLOADS_SESSION_KEY, str(upload.uuid))


def remove_submission_uploads_from_session(
    submission: Submission, session: SessionBase
) -> None:
    for attachment in submission.get_attachments().filter(temporary_file__isnull=False):
        remove_upload_from_session(attachment.temporary_file, session)


def send_confirmation_email(submission: Submission):
    logevent.confirmation_email_start(submission)

    try:
        subject_template, content_template = get_confirmation_email_templates(
            submission
        )
    except SkipConfirmationEmail:
        logger.debug(
            "Form %d is configured to not send a confirmation email for submission %d, "
            "skipping the confirmation e-mail.",
            submission.form.id,
            submission.id,
        )
        logevent.confirmation_email_skip(submission)
        return

    to_emails = submission.get_email_confirmation_recipients(submission.data)
    if not to_emails:
        logger.warning(
            "Could not determine the recipient e-mail address for submission %d, "
            "skipping the confirmation e-mail.",
            submission.id,
        )
        logevent.confirmation_email_skip(submission)
        return

    context = get_confirmation_email_context_data(submission)

    # render the templates with the submission context
    subject = render_email_template(
        subject_template, context, rendering_text=True
    ).strip()

    if subject_suffix := get_confirmation_mail_suffix(submission):
        subject = f"{subject} {subject_suffix}"

    html_content = render_email_template(content_template, context)
    text_content = strip_tags_plus(
        render_email_template(content_template, context, rendering_text=True),
        keep_leading_whitespace=True,
    )

    try:
        send_mail_html(
            subject,
            html_content,
            settings.DEFAULT_FROM_EMAIL,  # TODO: add config option to specify sender e-mail
            to_emails,
            text_message=text_content,
        )
    except Exception as e:
        logevent.confirmation_email_failure(submission, e)
        raise

    submission.confirmation_email_sent = True
    submission.save(update_fields=("confirmation_email_sent",))

    logevent.confirmation_email_success(submission)


def persist_user_defined_variables_unrelated_to_a_step(
    data: dict, submission: Submission
) -> None:
    keys_in_data = [key for key, value in data.items()]
    form_vars_keys = FormVariable.objects.filter(
        form=submission.form,
        key__in=keys_in_data,
        form_definition__isnull=True,
    ).values_list("key", flat=True)
    filtered_data = {key: value for key, value in data.items() if key in form_vars_keys}

    if filtered_data:
        SubmissionValueVariable.objects.bulk_create_or_update_from_data(
            filtered_data, submission
        )


def initialise_user_defined_variables(submission: Submission):
    state = submission.load_submission_value_variables_state()
    variables = {
        variable_key: variable
        for variable_key, variable in state.variables.items()
        if variable.form_variable.source == FormVariableSources.user_defined
    }
    SubmissionValueVariable.objects.bulk_create(
        [variable for key, variable in variables.items() if not variable.pk]
    )
