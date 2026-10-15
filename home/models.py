from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from core.blocks import HomeStreamBlock, SlideBlock


class HomePage(Page):
    slides = StreamField([("slide", SlideBlock())], blank=True, help_text="The rotating banner at the top. One slide shows without rotating.")

    body = StreamField(HomeStreamBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("slides"),
        FieldPanel("body"),
    ]

    max_count = 1
