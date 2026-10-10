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

    def test_form_finder_lists_feeding_forms(self):
        response = self.client.get("/get-started/")
        self.assertContains(response, "ST/OT Feeding Intake Form")
        self.assertContains(response, "data-finder-option")

    def test_who_we_help_merges_conditions_across_services(self):
        response = self.client.get("/services/")
        self.assertContains(response, 'id="who-we-help"')
        # Autism is listed on both OT and Speech, so it appears once with both chips.
        self.assertContains(response, 'data-condition="autism spectrum disorder"', count=1)
        row = response.content.decode().split('data-condition="autism spectrum disorder"')[1].split("</li>")[0]
        self.assertIn("/services/pediatric-occupational-therapy/", row)
        self.assertIn("/services/speech-language-therapy/", row)

    def test_insurance_page_linked_from_footer(self):
        self.assertContains(self.client.get("/"), 'href="/insurance/"')

    def test_contact_form_submits(self):
        response = self.client.post("/contact/", {
            "your_name": "Test Parent", "phone": "555-555-5555", "email": "parent@example.com",
            "im_interested_in": "Not sure yet", "how_can_we_help": "Hello",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thanks for reaching out")

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
        self.assertContains(response, 'href="/services/#who-we-help"')
