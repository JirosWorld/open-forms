from django.test import RequestFactory, TestCase
from django.urls import reverse

from furl import furl

from openforms.forms.tests.factories import FormStepFactory
from openforms.submissions.tests.factories import SubmissionFactory

from ..utils import get_cosign_login_info, store_auth_details, store_registrator_details


class UtilsTests(TestCase):
    def test_store_auth_details(self):
        submission = SubmissionFactory.create()

        with self.assertRaises(ValueError):
            store_auth_details(
                submission,
                {"plugin": "digid", "attribute": "WRONG", "value": "some-value"},
            )

    def test_store_registrator_details(self):
        submission = SubmissionFactory.create()

        with self.assertRaises(ValueError):
            store_registrator_details(
                submission,
                {"plugin": "digid", "attribute": "WRONG", "value": "some-value"},
            )

    def test_get_cosign_info_when_no_cosign_on_form(self):
        form_step = FormStepFactory.create(
            form_definition__configuration={
                "components": [
                    {"key": "textField", "label": "Not cosign", "type": "textfield"}
                ]
            }
        )

        factory = RequestFactory()
        request = factory.get("/foo")

        login_info = get_cosign_login_info(request=request, form=form_step.form)

        self.assertIsNone(login_info)

    def test_get_cosign_info(self):
        form_step = FormStepFactory.create(
            form__slug="form-with-cosign",
            form_definition__configuration={
                "components": [
                    {
                        "key": "cosignField",
                        "label": "Cosign",
                        "type": "cosign",
                        "authPlugin": "digid",
                    }
                ]
            },
        )

        factory = RequestFactory()
        request = factory.get("/foo")

        login_info = get_cosign_login_info(request=request, form=form_step.form)

        self.assertIsNotNone(login_info)

        login_url = furl(login_info.url)
        submission_find_url = furl(
            login_url.args["next"]
        )  # Page where the user will look for the submission to cosign

        self.assertEqual(
            login_url.path,
            reverse(
                "authentication:start",
                kwargs={
                    "slug": "form-with-cosign",
                    "plugin_id": "digid",
                },
            ),
        )
        self.assertEqual(
            submission_find_url.path,
            reverse(
                "submissions:find-submission-for-cosign",
                kwargs={"form_slug": "form-with-cosign"},
            ),
        )
