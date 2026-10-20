from django.core.management import call_command
from django.test import TestCase
from wagtail.contrib.forms.models import FormSubmission

from pages.models import ContactPage

CONTACT_POST = {
    "your_name": "Test Parent", "phone": "555-555-5555", "email": "parent@example.com",
    "im_interested_in": "Not sure yet", "how_can_we_help": "Hello",
}


class SeededSiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_site", verbosity=0)

    def test_pages_render(self):
        for url in [
            "/", "/about-us/", "/services/", "/services/pediatric-audiology/", "/our-providers/",
            "/our-providers/kimberly-oviedo/", "/get-started/", "/resources/", "/contact/",
            "/careers/", "/veterans/", "/hipaa-privacy-policy/", "/insurance/", "/search/?query=feeding",
        ]:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_unknown_provider_is_404(self):
        self.assertEqual(self.client.get("/our-providers/nobody/").status_code, 404)

    def test_veterans_link_on_every_page(self):
        for url in ["/", "/services/", "/get-started/"]:
            with self.subTest(url=url):
                self.assertContains(self.client.get(url), 'href="/veterans/"')

    def test_form_finder_combines_therapy_forms(self):
        response = self.client.get("/get-started/")
        self.assertContains(response, "data-finder-multi")
        # General Admissions is listed once and always shown; each therapy form only for its answer.
        self.assertContains(response, "<strong>General Admissions Form</strong>", count=1)
        self.assertContains(response, '<li class="doc-list__item" data-finder-for="1">')
        self.assertContains(response, "https://beyond-limits.secure-form.com/feeding-n/", count=2)  # new, and adding a therapy
        self.assertContains(response, "https://beyond-limits.secure-form.com/st-patient/", count=1)  # adding a therapy only
        self.assertNotContains(response, "Upper Extremity")

    def test_seeded_headshots_replace_initials(self):
        from pages.models import TeamMember

        kimberly = TeamMember.objects.get(slug="kimberly-oviedo")
        self.assertIsNotNone(kimberly.photo)
        self.assertTrue(kimberly.photo.has_focal_point())
        profile = self.client.get("/our-providers/kimberly-oviedo/").content.decode()
        photo_box = profile.split('class="profile__photo', 1)[1].split("</div>", 1)[0]
        self.assertIn("<img", photo_box)
        self.assertIsNone(TeamMember.objects.exclude(slug__in=["kimberly-oviedo", "karen-mobley", "ashley-moore"]).exclude(photo=None).first())

    def test_services_page_has_signs_cards(self):
        response = self.client.get("/services/")
        self.assertContains(response, 'id="does-this-sound-like-your-child"')
        self.assertContains(response, 'class="signs__card ', count=6)
        self.assertContains(response, 'href="/services/speech-language-therapy/"')
        self.assertNotContains(response, "data-conditions")

    def test_insurance_page_linked_from_footer(self):
        self.assertContains(self.client.get("/"), 'href="/insurance/"')

    def test_contact_form_submits_without_luxsci(self):
        ContactPage.objects.update(luxsci_form_id="")
        response = self.client.post("/contact/", CONTACT_POST)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thanks for reaching out")

    def test_contact_page_refuses_direct_posts_with_luxsci(self):
        response = self.client.post("/contact/", CONTACT_POST)
        self.assertEqual(response.status_code, 405)
        self.assertFalse(FormSubmission.objects.exists())

    def test_contact_dropdown_starts_on_not_sure(self):
        html = self.client.get("/contact/").content.decode()
        first_option = html.split('name="im_interested_in"')[1].split("<option")[1]
        self.assertIn("Not sure yet", first_option)

    def test_first_visit_photo_story(self):
        response = self.client.get("/first-visit/")
        self.assertContains(response, 'class="story__step"', count=9)
        self.assertContains(response, "data-print")
        for url in ["/services/pediatric-audiology/", "/contact/", "/insurance/"]:
            with self.subTest(url=url):
                self.assertContains(self.client.get(url), 'href="/first-visit/"')

    def test_home_slides_share_one_photo_frame(self):
        response = self.client.get("/")
        self.assertContains(response, "data-slider-frame", count=1)
        self.assertContains(response, "data-slider-visual", count=4)
        self.assertContains(response, 'href="/services/#does-this-sound-like-your-child"')

    def test_contact_form_posts_to_luxsci(self):
        response = self.client.get("/contact/")
        self.assertContains(response, 'name="secureform"')
        self.assertContains(response, 'action="https://secureform.luxsci.com/perl/post/18249-26830-Zg4g"')
        self.assertContains(response, "return secureform_submit();")
        self.assertContains(response, 'id="secureform-missing"')
        self.assertContains(response, "secureform.php?v=1&amp;c=18249-26830-Zg4g&amp;f=secureform")
        self.assertNotContains(response, "csrfmiddlewaretoken")
        self.assertContains(self.client.get("/contact/?sent=1"), 'class="form-thanks"')


class AdminLockoutTests(TestCase):
    def test_five_wrong_passwords_lock_the_login(self):
        from django.contrib.auth import get_user_model

        get_user_model().objects.create_superuser("staff", "staff@example.com", "right-password-123")
        for _ in range(5):
            self.client.post("/admin/login/", {"username": "staff", "password": "wrong"})
        response = self.client.post("/admin/login/", {"username": "staff", "password": "right-password-123"})
        self.assertEqual(response.status_code, 429)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_django_admin_is_not_public(self):
        self.assertEqual(self.client.get("/django-admin/").status_code, 404)

    def test_lockout_tracks_each_visitor_by_their_cloudflare_address(self):
        from django.contrib.auth import get_user_model

        get_user_model().objects.create_superuser("staff", "staff@example.com", "right-password-123")
        # What Render sends: the visitor, a Cloudflare edge, then Render's proxy.
        stranger = {"HTTP_CF_CONNECTING_IP": "198.51.100.9", "HTTP_X_FORWARDED_FOR": "198.51.100.9, 172.71.147.234, 10.24.43.5"}
        admin = {"HTTP_CF_CONNECTING_IP": "203.0.113.7", "HTTP_X_FORWARDED_FOR": "203.0.113.7, 172.71.147.234, 10.24.43.5"}
        for _ in range(5):
            self.client.post("/admin/login/", {"username": "staff", "password": "wrong"}, **stranger)
        self.assertEqual(self.client.post("/admin/login/", {"username": "staff", "password": "right-password-123"}, **stranger).status_code, 429)
        self.client.post("/admin/login/", {"username": "staff", "password": "right-password-123"}, **admin)
        self.assertIn("_auth_user_id", self.client.session)

    def test_client_ip_ignores_faked_forwarded_entries(self):
        from django.test import RequestFactory

        from core.security import client_ip

        factory = RequestFactory()
        faked = factory.get("/", HTTP_CF_CONNECTING_IP="203.0.113.7", HTTP_X_FORWARDED_FOR="1.2.3.4, 203.0.113.7, 172.71.147.234, 10.24.43.5")
        self.assertEqual(client_ip(faked), "203.0.113.7")
        no_cloudflare = factory.get("/", HTTP_X_FORWARDED_FOR="1.2.3.4, 10.0.0.1")
        self.assertEqual(client_ip(no_cloudflare), "10.0.0.1")
