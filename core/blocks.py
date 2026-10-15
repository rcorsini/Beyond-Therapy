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
    ("door", "Door"),
    ("car", "Car"),
    ("toilet", "Bathroom"),
    ("users", "People"),
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
            anchor = (self.get("anchor") or "").lstrip("#")
            return f"{page.url}#{anchor}" if anchor else page.url
        return self.get("external_url") or ""


class LinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False)
    page = blocks.PageChooserBlock(required=False)
    external_url = blocks.URLBlock(required=False, label="Or a web address")
    anchor = blocks.CharBlock(required=False, help_text="Optional. Jump to a section of the chosen page, e.g. does-this-sound-like-your-child.")

    class Meta:
        value_class = LinkStructValue
        icon = "link"


class HeadingBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, help_text="Small line above the heading.")
    heading = blocks.CharBlock()
    intro = blocks.TextBlock(required=False)

    class Meta:
        icon = "title"
        template = "core/blocks/heading_block.html"


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


class ConditionsBlock(blocks.StructBlock):
    """Every condition listed on the service pages, with the therapies that help.

    Built from each service's "Helps with" list, so it stays in sync with them.
    Conditions with the same wording on several services are merged into one row.
    """

    heading = HeadingBlock()
    filter_label = blocks.CharBlock(default="Search for a concern", required=False)

    class Meta:
        icon = "search"
        template = "core/blocks/conditions.html"

    def get_context(self, value, parent_context=None):
        from pages.models import ServicePage

        context = super().get_context(value, parent_context)
        rows = {}
        for service in ServicePage.objects.live().public().order_by("path"):
            for name in service.helps_with_list():
                row = rows.setdefault(name.lower(), {"name": name, "services": []})
                row["services"].append(service)
        context["conditions"] = sorted(rows.values(), key=lambda r: r["name"].lower())
        return context


class SignsBlock(blocks.StructBlock):
    """"Does this sound like your child?" cards: everyday signs a parent might
    notice, each pointing to the therapy that helps."""

    heading = HeadingBlock()
    anchor = blocks.CharBlock(
        default="does-this-sound-like-your-child",
        help_text="Lets buttons jump straight to this section. Change it only if you also update those links.",
    )
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock()),
                ("icon", blocks.ChoiceBlock(choices=ICON_CHOICES, default="star")),
                ("color", blocks.ChoiceBlock(choices=COLOR_CHOICES, default="sky")),
                ("signs", blocks.TextBlock(help_text="One sign per line, in the words a parent would use.")),
                ("link", LinkBlock()),
            ],
            icon="help",
        )
    )

    class Meta:
        icon = "help"
        label = "Does this sound like your child?"
        template = "core/blocks/signs.html"


class VisitStoryBlock(blocks.StructBlock):
    """A step-by-step photo story of a first visit, written for the child.

    Children who know what is coming often feel calmer. Families can look
    through it together at home, or print it.
    """

    heading = blocks.CharBlock(default="Your first visit, one step at a time")
    parent_note = blocks.TextBlock(required=False, help_text="A short note for grown-ups at the top.")
    steps = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("photo", ImageChooserBlock(required=False, help_text="A real photo of this spot, cropped to a 4:3 rectangle around the image's focal point. Until there is one, the icon is shown.")),
                ("icon", blocks.ChoiceBlock(choices=ICON_CHOICES, default="star")),
                ("text", blocks.CharBlock(help_text="One or two short sentences, written as the child: 'This is the front door.'")),
                ("alt", blocks.CharBlock(required=False, help_text="Describe the photo for screen readers, e.g. 'Glass front door with the Beyond Limits sign above it.'")),
            ],
            icon="image",
        )
    )

    class Meta:
        icon = "image"
        label = "First visit photo story"
        template = "core/blocks/visit_story.html"


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
    conditions = ConditionsBlock()
    visit_story = VisitStoryBlock()
    signs = SignsBlock()


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
    image = ImageChooserBlock(required=False, help_text="Shown in the round-topped frame on the right, cropped square around the focal point. Without one, the illustration below is shown.")
    background = blocks.ChoiceBlock(choices=COLOR_CHOICES + [("indigo", "Soft indigo")], default="indigo")
    illustration = blocks.ChoiceBlock(
        choices=[("hero", "Rainbow and blocks"), ("blocks", "Building blocks"), ("garden", "Garden"), ("team", "Team circle"), ("gym", "Therapy gym")],
        default="hero",
        help_text="Used when no photo is chosen.",
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
