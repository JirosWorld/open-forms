import shutil
import tempfile
from pathlib import Path

from django.conf import settings
from django.test import override_settings
from django.urls import reverse

from django_webtest import WebTest
from webtest import Upload

from openforms.accounts.tests.factories import SuperUserFactory
from openforms.forms.tests.factories import FormFactory
from openforms.tests.utils import disable_2fa

from .factories import ThemeFactory

LOGO_FILE = Path(settings.BASE_DIR) / "docs" / "logo.svg"


@disable_2fa
@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class AdminTests(WebTest):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.user = SuperUserFactory.create()

    def setUp(self):
        super().setUp()

        self.app.set_user(self.user)

        def _cleanup():
            try:
                shutil.rmtree(settings.MEDIA_ROOT)
            except Exception:
                pass

        self.addCleanup(_cleanup)

    def test_upload_svg(self):

        with self.subTest(part="admin config"):
            theme = ThemeFactory.create()
            url = reverse("admin:config_theme_change", args=(theme.pk,))

            change_page = self.app.get(url)

            with open(LOGO_FILE, "rb") as infile:
                upload = Upload("logo.svg", infile.read(), "image/svg+xml")

            change_page.form["logo"] = upload
            response = change_page.form.submit()

            self.assertEqual(response.status_code, 302)
            theme.refresh_from_db()
            self.assertEqual(theme.logo, "logo/logo.svg")

        with self.subTest(part="logo used"):
            form = FormFactory.create(theme=theme)
            url = reverse("forms:form-detail", kwargs={"slug": form.slug})

            form_page = self.app.get(url)

            header = form_page.pyquery(".utrecht-page-header")
            self.assertTrue(header)
            self.assertIn(
                "utrecht-page-header--openforms-with-logo", header.attr("class")
            )

            style_tag = form_page.pyquery("style")
            self.assertIn(
                f"--of-header-logo-url: url('{theme.logo.url}')",
                style_tag.text(),
            )

    def test_upload_png(self):
        logo = Path(settings.DJANGO_PROJECT_DIR) / "static" / "img" / "digid.png"
        theme = ThemeFactory.create()
        url = reverse("admin:config_theme_change", args=(theme.pk,))

        change_page = self.app.get(url)

        with open(logo, "rb") as infile:
            upload = Upload("digid.png", infile.read(), "image/png")

        change_page.form["logo"] = upload
        response = change_page.form.submit()

        self.assertEqual(response.status_code, 302)
        theme.refresh_from_db()
        self.assertEqual(theme.logo, "logo/digid.png")

    def test_upload_blank(self):
        # fixes #581
        theme = ThemeFactory.create()
        url = reverse("admin:config_theme_change", args=(theme.pk,))
        change_page = self.app.get(url)

        response = change_page.form.submit()

        self.assertEqual(response.status_code, 302)
        theme.refresh_from_db()
        self.assertEqual(theme.logo, "")

    def test_can_upload_stylesheet(self):
        theme = ThemeFactory.create()
        url = reverse("admin:config_theme_change", args=(theme.pk,))
        upload = Upload("my-theme.css", b".foo { display: block }", "text/css")

        change_page = self.app.get(url)

        change_page.form["stylesheet_file"] = upload
        response = change_page.form.submit()

        self.assertEqual(response.status_code, 302)
        theme.refresh_from_db()
        self.assertEqual(theme.stylesheet_file, "config/themes/my-theme.css")
