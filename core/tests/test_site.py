from django.core.management import call_command
from django.test import TestCase


class SeededSiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_site", verbosity=0)

    def test_pages_render(self):
        for url in [
            "/", "/about-us/", "/services/", "/services/pediatric-audiology/", "/our-providers/",
            "/our-providers/kimberly-oviedo/", "/get-started/", "/resources/", "/contact/",
            "/careers/", "/veterans/", "/hipaa-privacy-policy/", "/search/?query=feeding",
        ]:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_unknown_provider_is_404(self):
        self.assertEqual(self.client.get("/our-providers/nobody/").status_code, 404)

    def test_veterans_link_on_every_page(self):
        for url in ["/", "/services/", "/get-started/"]:
            with self.subTest(url=url):
                self.assertContains(self.client.get(url), 'href="/veterans/"')

    def test_form_finder_lists_feeding_forms(self):
        response = self.client.get("/get-started/")
        self.assertContains(response, "ST/OT Feeding Intake Form")
        self.assertContains(response, "data-finder-option")

    def test_contact_form_submits(self):
        response = self.client.post("/contact/", {
            "your_name": "Test Parent", "phone": "555-555-5555", "email": "parent@example.com",
            "im_interested_in": "Not sure yet", "how_can_we_help": "Hello",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thanks for reaching out")
