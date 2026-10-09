from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting


@register_setting(icon="site")
class ClinicSettings(BaseGenericSetting):
    """Contact details and global links shown in the header and footer."""

    clinic_name = models.CharField(max_length=120, default="Beyond Limits Pediatric Therapy Center")
    short_name = models.CharField(max_length=60, default="Beyond Limits")
    tagline = models.CharField(max_length=160, blank=True, default="Helping kids thrive, birth to 21.")
    logo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+",
        help_text="The Beyond Limits logo. Without one, a simple placeholder mark is shown.",
    )

    phone = models.CharField(max_length=30, blank=True, help_text="Shown as 'Call or text'.")
    fax = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address_line_1 = models.CharField(max_length=120, blank=True)
    address_line_2 = models.CharField(max_length=120, blank=True)
    hours = models.CharField(max_length=120, blank=True)
    map_embed_url = models.URLField(blank=True, help_text="Embed URL for the map on the contact page.")
    directions_url = models.URLField(blank=True)

    start_page = models.ForeignKey(
        "wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL, related_name="+",
        help_text="Where the 'Start here' button goes (usually Get Started).",
    )
    veterans_page = models.ForeignKey(
        "wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL, related_name="+",
        help_text="Linked from the top bar and footer so veterans always find it.",
    )
    veterans_label = models.CharField(max_length=60, default="Veterans hearing exams")
    careers_page = models.ForeignKey(
        "wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL, related_name="+",
    )
    privacy_page = models.ForeignKey(
        "wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL, related_name="+",
    )

    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    panels = [
        MultiFieldPanel([FieldPanel("clinic_name"), FieldPanel("short_name"), FieldPanel("tagline"), FieldPanel("logo")], "Name"),
        MultiFieldPanel(
            [
                FieldPanel("phone"), FieldPanel("fax"), FieldPanel("email"),
                FieldPanel("address_line_1"), FieldPanel("address_line_2"), FieldPanel("hours"),
                FieldPanel("map_embed_url"), FieldPanel("directions_url"),
            ],
            "Contact",
        ),
        MultiFieldPanel(
            [
                FieldPanel("start_page"), FieldPanel("veterans_page"), FieldPanel("veterans_label"),
                FieldPanel("careers_page"), FieldPanel("privacy_page"),
            ],
            "Global links",
        ),
        MultiFieldPanel(
            [FieldPanel("facebook_url"), FieldPanel("instagram_url"), FieldPanel("youtube_url"), FieldPanel("linkedin_url")],
            "Social",
        ),
    ]

    class Meta:
        verbose_name = "Clinic settings"

    @property
    def phone_digits(self):
        return "".join(c for c in self.phone if c.isdigit())
