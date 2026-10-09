from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

ICON_CHOICES = [
    ("ear", "Ear (audiology)"),
    ("hand", "Hand (occupational therapy)"),
    ("run", "Runner (physical therapy)"),
    ("speech", "Speech bubble (speech therapy)"),
    ("heart", "Heart"),
    ("star", "Star"),
    ("sun", "Sun"),
    ("puzzle", "Puzzle piece"),
    ("family", "Family"),
    ("home", "Home"),
    ("calendar", "Calendar"),
    ("clipboard", "Clipboard"),
    ("shield", "Shield"),
    ("sparkle", "Sparkle"),
    ("book", "Book"),
    ("grad", "Graduation cap"),
    ("chat", "Chat"),
    ("check", "Check"),
    ("flag", "Flag"),
    ("phone", "Phone"),
]

COLOR_CHOICES = [
    ("sun", "Sunny yellow"),
    ("coral", "Coral"),
    ("teal", "Teal"),
    ("sky", "Sky blue"),
    ("grape", "Grape"),
    ("leaf", "Leaf green"),
]


class LinkStructValue(blocks.StructValue):
    def url(self):
        page = self.get("page")
        if page:
            return page.url
        return self.get("external_url") or ""


class LinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False)
    page = blocks.PageChooserBlock(required=False)
    external_url = blocks.URLBlock(required=False, label="Or a web address")

    class Meta:
        value_class = LinkStructValue
        icon = "link"


class HeadingBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, help_text="Small line above the heading.")
    heading = blocks.CharBlock()
    intro = blocks.TextBlock(required=False)

    class Meta:
        icon = "title"
        template = "core/blocks/heading.html"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)
    shape = blocks.ChoiceBlock(
        choices=[("blob", "Soft blob"), ("rounded", "Rounded rectangle")], default="rounded"
    )

    class Meta:
        icon = "image"
        template = "core/blocks/image.html"


class CardBlock(blocks.StructBlock):
    icon = blocks.ChoiceBlock(choices=ICON_CHOICES, default="star")
    color = blocks.ChoiceBlock(choices=COLOR_CHOICES, default="sun")
    title = blocks.CharBlock()
    text = blocks.TextBlock(required=False)
    link = LinkBlock(required=False)


class CardGridBlock(blocks.StructBlock):
    heading = HeadingBlock(required=False)
    cards = blocks.ListBlock(CardBlock())

    class Meta:
        icon = "table"
        template = "core/blocks/card_grid.html"


class StepsBlock(blocks.StructBlock):
    heading = HeadingBlock(required=False)
    steps = blocks.ListBlock(
        blocks.StructBlock(
            [("title", blocks.CharBlock()), ("text", blocks.TextBlock(required=False)), ("link", LinkBlock(required=False))]
        )
    )

    class Meta:
        icon = "list-ol"
        template = "core/blocks/steps.html"


class ChecklistBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    color = blocks.ChoiceBlock(choices=COLOR_CHOICES, default="teal")
    items = blocks.ListBlock(blocks.CharBlock())

    class Meta:
        icon = "tick"
        template = "core/blocks/checklist.html"


class CalloutBlock(blocks.StructBlock):
    color = blocks.ChoiceBlock(choices=COLOR_CHOICES, default="sun")
    icon = blocks.ChoiceBlock(choices=ICON_CHOICES, default="sparkle")
    title = blocks.CharBlock()
    text = blocks.RichTextBlock(features=["bold", "italic", "link"], required=False)
    button = LinkBlock(required=False)

    class Meta:
        icon = "pick"
        template = "core/blocks/callout.html"


class FAQBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="Common questions")
    items = blocks.ListBlock(
        blocks.StructBlock([("question", blocks.CharBlock()), ("answer", blocks.RichTextBlock(features=["bold", "italic", "link", "ul"]))])
    )

    class Meta:
        icon = "help"
        template = "core/blocks/faq.html"


class LinkListBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    links = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock()),
                ("url", blocks.URLBlock(required=False)),
                ("description", blocks.CharBlock(required=False)),
            ]
        )
    )

    class Meta:
        icon = "link"
        template = "core/blocks/link_list.html"


class DocumentListBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    intro = blocks.TextBlock(required=False)
    documents = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock()),
                ("document", DocumentChooserBlock(required=False)),
                ("note", blocks.CharBlock(required=False, help_text="e.g. 'For newborns to 12 months'")),
            ]
        )
    )

    class Meta:
        icon = "doc-full"
        template = "core/blocks/document_list.html"


class TestimonialBlock(blocks.StructBlock):
    quote = blocks.TextBlock()
    name = blocks.CharBlock()
    role = blocks.CharBlock(required=False, help_text="e.g. 'Grace's mom'")

    class Meta:
        icon = "openquote"
        template = "core/blocks/testimonial.html"


class StatsBlock(blocks.StructBlock):
    stats = blocks.ListBlock(
        blocks.StructBlock([("number", blocks.CharBlock()), ("label", blocks.CharBlock())])
    )

    class Meta:
        icon = "order"
        template = "core/blocks/stats.html"


class CTABannerBlock(blocks.StructBlock):
    color = blocks.ChoiceBlock(choices=COLOR_CHOICES, default="teal")
    title = blocks.CharBlock()
    text = blocks.TextBlock(required=False)
    button = LinkBlock()
    secondary_button = LinkBlock(required=False)

    class Meta:
        icon = "pick"
        template = "core/blocks/cta_banner.html"


class SplitBlock(blocks.StructBlock):
    """Text on one side, image on the other."""

    eyebrow = blocks.CharBlock(required=False)
    heading = blocks.CharBlock()
    text = blocks.RichTextBlock(features=["bold", "italic", "link", "ul", "ol"])
    image = ImageChooserBlock(required=False)
    illustration = blocks.ChoiceBlock(
        choices=[("blocks", "Building blocks"), ("garden", "Garden"), ("team", "Team circle"), ("gym", "Therapy gym")],
        default="blocks",
        help_text="Shown when no image is chosen.",
    )
    image_side = blocks.ChoiceBlock(choices=[("right", "Right"), ("left", "Left")], default="right")
    button = LinkBlock(required=False)

    class Meta:
        icon = "doc-full-inverse"
        template = "core/blocks/split.html"


class FormItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    online_url = blocks.URLBlock(required=False, help_text="Secure online form (e.g. LuxSci). Shown as 'Fill out online'.")
    document = DocumentChooserBlock(required=False, help_text="Printable PDF, if there is one.")
    note = blocks.CharBlock(required=False, help_text="e.g. 'Only if you'll use telehealth'")


class FormFinderOptionBlock(blocks.StructBlock):
    label = blocks.CharBlock()
    forms = blocks.ListBlock(FormItemBlock(), required=False)
    note = blocks.RichTextBlock(features=["bold", "italic", "link"], required=False)


class FormFinderPathBlock(blocks.StructBlock):
    label = blocks.CharBlock(help_text="e.g. 'My child is new to Beyond Limits'")
    description = blocks.CharBlock(required=False)
    icon = blocks.ChoiceBlock(choices=ICON_CHOICES, default="family")
    follow_up_question = blocks.CharBlock(required=False, help_text="Asked when this path has options, e.g. 'Which service is your child starting?'")
    options = blocks.ListBlock(FormFinderOptionBlock(), required=False, help_text="Leave empty to go straight to the forms below.")
    forms = blocks.ListBlock(FormItemBlock(), required=False, help_text="Forms for everyone on this path (added to any option's forms).")
    note = blocks.RichTextBlock(features=["bold", "italic", "link"], required=False)
    button = LinkBlock(required=False)


class FormFinderBlock(blocks.StructBlock):
    """A guided 'which forms do I need?' chooser. Without JavaScript every path is listed."""

    heading = HeadingBlock(required=False)
    question = blocks.CharBlock(default="What brings you here today?")
    paths = blocks.ListBlock(FormFinderPathBlock())
    return_note = blocks.RichTextBlock(
        features=["bold", "italic", "link"], required=False,
        help_text="How to send the forms back. Shown with every result.",
    )

    class Meta:
        icon = "help"
        template = "core/blocks/form_finder.html"


class BodyStreamBlock(blocks.StreamBlock):
    heading = HeadingBlock()
    paragraph = blocks.RichTextBlock(
        features=["h2", "h3", "bold", "italic", "link", "ol", "ul", "document-link"],
        template="core/blocks/paragraph.html",
    )
    split = SplitBlock()
    image = ImageBlock()
    cards = CardGridBlock()
    steps = StepsBlock()
    checklist = ChecklistBlock()
    callout = CalloutBlock()
    faq = FAQBlock()
    links = LinkListBlock()
    documents = DocumentListBlock()
    testimonial = TestimonialBlock()
    stats = StatsBlock()
    cta = CTABannerBlock()
    form_finder = FormFinderBlock()


class ServicesOverviewBlock(blocks.StructBlock):
    """Cards for every published service page, pulled in automatically."""

    heading = HeadingBlock()

    class Meta:
        icon = "list-ul"
        template = "core/blocks/services_overview.html"

    def get_context(self, value, parent_context=None):
        from pages.models import ServicePage

        context = super().get_context(value, parent_context)
        context["services"] = ServicePage.objects.live().public().filter(show_in_overview=True).order_by("path")
        return context


class TeamTeaserBlock(blocks.StructBlock):
    """A row of team faces, pulled in automatically."""

    heading = HeadingBlock()
    count = blocks.IntegerBlock(default=8, min_value=3, max_value=16)
    button = LinkBlock(required=False)

    class Meta:
        icon = "group"
        template = "core/blocks/team_teaser.html"

    def get_context(self, value, parent_context=None):
        from pages.models import TeamMember

        context = super().get_context(value, parent_context)
        members = TeamMember.objects.filter(is_clinician=True).order_by("?")[: value["count"]]
        context["members"] = members
        return context


class CareersBandBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, default="Work with us")
    heading = blocks.CharBlock()
    text = blocks.TextBlock(required=False)
    points = blocks.ListBlock(blocks.CharBlock(), required=False)
    button = LinkBlock()
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = "user"
        template = "core/blocks/careers_band.html"


class QuickLinksBlock(blocks.StructBlock):
    """Numbered tiles that overlap the bottom of the home slider."""

    links = blocks.ListBlock(
        blocks.StructBlock([("title", blocks.CharBlock()), ("text", blocks.CharBlock(required=False)), ("link", LinkBlock())]),
        max_num=4,
    )

    class Meta:
        icon = "list-ol"
        template = "core/blocks/quick_links.html"


class SlideBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False, help_text="Wide photo. Without one, a playful illustration is shown.")
    background = blocks.ChoiceBlock(choices=COLOR_CHOICES + [("indigo", "Soft indigo")], default="indigo")
    illustration = blocks.ChoiceBlock(
        choices=[("hero", "Rainbow and blocks"), ("blocks", "Building blocks"), ("garden", "Garden"), ("team", "Team circle"), ("gym", "Therapy gym")],
        default="hero",
    )
    box_color = blocks.ChoiceBlock(
        choices=[("indigo", "Indigo"), ("teal", "Green"), ("coral", "Red"), ("grape", "Grape"), ("sky", "Blue"), ("navy", "Navy")],
        default="indigo",
    )
    eyebrow = blocks.CharBlock(required=False)
    title = blocks.CharBlock()
    text = blocks.TextBlock(required=False)
    button = LinkBlock(required=False)
    note = blocks.CharBlock(required=False, help_text="Small line under the button.")

    class Meta:
        icon = "image"


class HomeStreamBlock(BodyStreamBlock):
    quick_links = QuickLinksBlock()
    services_overview = ServicesOverviewBlock()
    team_teaser = TeamTeaserBlock()
    careers_band = CareersBandBlock()
