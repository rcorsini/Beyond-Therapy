
import django.db.models.deletion
import modelcluster.fields
import modelsearch.index
import wagtail.contrib.forms.models
import wagtail.contrib.routable_page.models
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    # Replaces the original migration history, which databases created
    # before this squash have already applied.
    replaces = [("pages", "0001_initial"), ("pages", "0002_alter_careerspage_body_alter_jobpage_body_and_more"), ("pages", "0003_alter_careerspage_body_alter_jobpage_body_and_more"), ("pages", "0004_alter_careerspage_body_alter_jobpage_body_and_more"), ("pages", "0005_alter_teammember_options_and_more"), ("pages", "0006_servicepage_photo_alter_careerspage_body_and_more"), ("pages", "0007_contactpage_luxsci_form_id"), ("pages", "0008_teampage_group_photo_alter_careerspage_body_and_more"), ("pages", "0009_alter_careerspage_body_alter_jobpage_body_and_more")]

    initial = True

    dependencies = [
        ("wagtailcore", "0097_baselogentry_uuid_action_timestamp_indexes"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="CareersPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "hero_intro",
                    models.TextField(
                        blank=True,
                        help_text="One or two friendly sentences under the page title.",
                    ),
                ),
                (
                    "hero_color",
                    models.CharField(
                        choices=[
                            ("indigo", "Soft indigo"),
                            ("sun", "Sunny yellow"),
                            ("coral", "Coral"),
                            ("teal", "Teal"),
                            ("sky", "Sky blue"),
                            ("grape", "Grape"),
                            ("leaf", "Leaf green"),
                            ("navy", "Navy (veterans)"),
                        ],
                        default="indigo",
                        max_length=10,
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", 3),
                            ("paragraph", 4),
                            ("split", 14),
                            ("image", 17),
                            ("cards", 23),
                            ("steps", 26),
                            ("checklist", 28),
                            ("callout", 30),
                            ("faq", 35),
                            ("links", 39),
                            ("documents", 44),
                            ("testimonial", 47),
                            ("stats", 50),
                            ("cta", 52),
                            ("form_finder", 67),
                            ("conditions", 69),
                            ("visit_story", 77),
                            ("signs", 82),
                        ],
                        blank=True,
                        block_lookup={
                            0: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Small line above the heading.",
                                    "required": False,
                                },
                            ),
                            1: ("wagtail.blocks.CharBlock", (), {}),
                            2: ("wagtail.blocks.TextBlock", (), {"required": False}),
                            3: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {},
                            ),
                            4: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": [
                                        "h2",
                                        "h3",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ol",
                                        "ul",
                                        "document-link",
                                    ],
                                    "template": "core/blocks/paragraph.html",
                                },
                            ),
                            5: ("wagtail.blocks.CharBlock", (), {"required": False}),
                            6: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul", "ol"]},
                            ),
                            7: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            8: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blocks", "Building blocks"),
                                        ("garden", "Garden"),
                                        ("team", "Team circle"),
                                        ("gym", "Therapy gym"),
                                    ],
                                    "help_text": "Shown when no image is chosen.",
                                },
                            ),
                            9: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {"choices": [("right", "Right"), ("left", "Left")]},
                            ),
                            10: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            11: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "Or a web address", "required": False},
                            ),
                            12: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Optional. Jump to a section of the chosen page, e.g. does-this-sound-like-your-child.",
                                    "required": False,
                                },
                            ),
                            13: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {"required": False},
                            ),
                            14: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("eyebrow", 5),
                                        ("heading", 1),
                                        ("text", 6),
                                        ("image", 7),
                                        ("illustration", 8),
                                        ("image_side", 9),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            15: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                            16: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blob", "Soft blob"),
                                        ("rounded", "Rounded rectangle"),
                                    ]
                                },
                            ),
                            17: (
                                "wagtail.blocks.StructBlock",
                                [[("image", 15), ("caption", 5), ("shape", 16)]],
                                {},
                            ),
                            18: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {"required": False},
                            ),
                            19: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
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
                                },
                            ),
                            20: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("sun", "Sunny yellow"),
                                        ("coral", "Coral"),
                                        ("teal", "Teal"),
                                        ("sky", "Sky blue"),
                                        ("grape", "Grape"),
                                        ("leaf", "Leaf green"),
                                    ]
                                },
                            ),
                            21: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("icon", 19),
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("link", 13),
                                    ]
                                ],
                                {},
                            ),
                            22: ("wagtail.blocks.ListBlock", (21,), {}),
                            23: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("cards", 22)]],
                                {},
                            ),
                            24: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("text", 2), ("link", 13)]],
                                {},
                            ),
                            25: ("wagtail.blocks.ListBlock", (24,), {}),
                            26: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("steps", 25)]],
                                {},
                            ),
                            27: ("wagtail.blocks.ListBlock", (1,), {}),
                            28: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 5), ("color", 20), ("items", 27)]],
                                {},
                            ),
                            29: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "required": False,
                                },
                            ),
                            30: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("icon", 19),
                                        ("title", 1),
                                        ("text", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            31: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Common questions", "required": False},
                            ),
                            32: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul"]},
                            ),
                            33: (
                                "wagtail.blocks.StructBlock",
                                [[("question", 1), ("answer", 32)]],
                                {},
                            ),
                            34: ("wagtail.blocks.ListBlock", (33,), {}),
                            35: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 31), ("items", 34)]],
                                {},
                            ),
                            36: ("wagtail.blocks.URLBlock", (), {"required": False}),
                            37: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("url", 36), ("description", 5)]],
                                {},
                            ),
                            38: ("wagtail.blocks.ListBlock", (37,), {}),
                            39: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("links", 38)]],
                                {},
                            ),
                            40: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {"required": False},
                            ),
                            41: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'For newborns to 12 months'",
                                    "required": False,
                                },
                            ),
                            42: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("document", 40), ("note", 41)]],
                                {},
                            ),
                            43: ("wagtail.blocks.ListBlock", (42,), {}),
                            44: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("intro", 2), ("documents", 43)]],
                                {},
                            ),
                            45: ("wagtail.blocks.TextBlock", (), {}),
                            46: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"help_text": "e.g. 'Grace's mom'", "required": False},
                            ),
                            47: (
                                "wagtail.blocks.StructBlock",
                                [[("quote", 45), ("name", 1), ("role", 46)]],
                                {},
                            ),
                            48: (
                                "wagtail.blocks.StructBlock",
                                [[("number", 1), ("label", 1)]],
                                {},
                            ),
                            49: ("wagtail.blocks.ListBlock", (48,), {}),
                            50: ("wagtail.blocks.StructBlock", [[("stats", 49)]], {}),
                            51: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {},
                            ),
                            52: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("button", 51),
                                        ("secondary_button", 13),
                                    ]
                                ],
                                {},
                            ),
                            53: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "What brings you here today?"},
                            ),
                            54: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'My child is new to Beyond Limits'"
                                },
                            ),
                            55: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Asked when this path has options, e.g. 'Which service is your child starting?'",
                                    "required": False,
                                },
                            ),
                            56: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {
                                    "help_text": "Secure online form (e.g. LuxSci). Shown as 'Fill out online'.",
                                    "required": False,
                                },
                            ),
                            57: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {
                                    "help_text": "Printable PDF, if there is one.",
                                    "required": False,
                                },
                            ),
                            58: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'Only if you'll use telehealth'",
                                    "required": False,
                                },
                            ),
                            59: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("online_url", 56),
                                        ("document", 57),
                                        ("note", 58),
                                    ]
                                ],
                                {},
                            ),
                            60: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {"required": False},
                            ),
                            61: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 1), ("forms", 60), ("note", 29)]],
                                {},
                            ),
                            62: (
                                "wagtail.blocks.ListBlock",
                                (61,),
                                {
                                    "help_text": "Leave empty to go straight to the forms below.",
                                    "required": False,
                                },
                            ),
                            63: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {
                                    "help_text": "Forms for everyone on this path (added to any option's forms).",
                                    "required": False,
                                },
                            ),
                            64: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 54),
                                        ("description", 5),
                                        ("icon", 19),
                                        ("follow_up_question", 55),
                                        ("options", 62),
                                        ("forms", 63),
                                        ("note", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            65: ("wagtail.blocks.ListBlock", (64,), {}),
                            66: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "help_text": "How to send the forms back. Shown with every result.",
                                    "required": False,
                                },
                            ),
                            67: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("heading", 18),
                                        ("question", 53),
                                        ("paths", 65),
                                        ("return_note", 66),
                                    ]
                                ],
                                {},
                            ),
                            68: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Search for a concern", "required": False},
                            ),
                            69: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("filter_label", 68)]],
                                {},
                            ),
                            70: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Your first visit, one step at a time"},
                            ),
                            71: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "A short note for grown-ups at the top.",
                                    "required": False,
                                },
                            ),
                            72: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "A real photo of this spot, cropped to a 4:3 rectangle around the image's focal point. Until there is one, the icon is shown.",
                                    "required": False,
                                },
                            ),
                            73: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "One or two short sentences, written as the child: 'This is the front door.'"
                                },
                            ),
                            74: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Describe the photo for screen readers, e.g. 'Glass front door with the Beyond Limits sign above it.'",
                                    "required": False,
                                },
                            ),
                            75: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("photo", 72),
                                        ("icon", 19),
                                        ("text", 73),
                                        ("alt", 74),
                                    ]
                                ],
                                {"icon": "image"},
                            ),
                            76: ("wagtail.blocks.ListBlock", (75,), {}),
                            77: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 70), ("parent_note", 71), ("steps", 76)]],
                                {},
                            ),
                            78: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "default": "does-this-sound-like-your-child",
                                    "help_text": "Lets buttons jump straight to this section. Change it only if you also update those links.",
                                },
                            ),
                            79: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "One sign per line, in the words a parent would use."
                                },
                            ),
                            80: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("icon", 19),
                                        ("color", 20),
                                        ("signs", 79),
                                        ("link", 51),
                                    ]
                                ],
                                {"icon": "help"},
                            ),
                            81: ("wagtail.blocks.ListBlock", (80,), {}),
                            82: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("anchor", 78), ("cards", 81)]],
                                {},
                            ),
                        },
                    ),
                ),
                (
                    "no_openings_text",
                    models.CharField(
                        blank=True,
                        default="No openings posted right now, but we always want to hear from great therapists.",
                        max_length=255,
                    ),
                ),
                ("general_apply_email", models.EmailField(blank=True, max_length=254)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="ContactPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "to_address",
                    models.CharField(
                        blank=True,
                        help_text="Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.",
                        max_length=255,
                        validators=[wagtail.contrib.forms.models.validate_to_address],
                        verbose_name="to address",
                    ),
                ),
                (
                    "from_address",
                    models.EmailField(
                        blank=True, max_length=255, verbose_name="from address"
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="subject"
                    ),
                ),
                (
                    "hero_intro",
                    models.TextField(
                        blank=True,
                        help_text="One or two friendly sentences under the page title.",
                    ),
                ),
                (
                    "hero_color",
                    models.CharField(
                        choices=[
                            ("indigo", "Soft indigo"),
                            ("sun", "Sunny yellow"),
                            ("coral", "Coral"),
                            ("teal", "Teal"),
                            ("sky", "Sky blue"),
                            ("grape", "Grape"),
                            ("leaf", "Leaf green"),
                            ("navy", "Navy (veterans)"),
                        ],
                        default="indigo",
                        max_length=10,
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
                ("thank_you_text", wagtail.fields.RichTextField(blank=True)),
                (
                    "luxsci_form_id",
                    models.CharField(
                        blank=True,
                        help_text="e.g. 18249-26830-Zg4g. When filled in, messages go to LuxSci (HIPAA-secure, with spam protection) instead of being saved in this admin. Leave blank to save messages here.",
                        max_length=60,
                        verbose_name="LuxSci Secure Form code",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail.contrib.forms.models.FormMixin,
                "wagtailcore.page",
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="JobPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "hero_intro",
                    models.TextField(
                        blank=True,
                        help_text="One or two friendly sentences under the page title.",
                    ),
                ),
                (
                    "hero_color",
                    models.CharField(
                        choices=[
                            ("indigo", "Soft indigo"),
                            ("sun", "Sunny yellow"),
                            ("coral", "Coral"),
                            ("teal", "Teal"),
                            ("sky", "Sky blue"),
                            ("grape", "Grape"),
                            ("leaf", "Leaf green"),
                            ("navy", "Navy (veterans)"),
                        ],
                        default="indigo",
                        max_length=10,
                    ),
                ),
                (
                    "discipline",
                    models.CharField(
                        choices=[
                            ("audiology", "Audiology"),
                            ("ot", "Occupational Therapy"),
                            ("pt", "Physical Therapy"),
                            ("slp", "Speech-Language Pathology"),
                            ("office", "Front Office & Leadership"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "employment_type",
                    models.CharField(default="Full-time", max_length=40),
                ),
                ("location", models.CharField(default="Acworth, GA", max_length=80)),
                ("summary", models.TextField()),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", 3),
                            ("paragraph", 4),
                            ("split", 14),
                            ("image", 17),
                            ("cards", 23),
                            ("steps", 26),
                            ("checklist", 28),
                            ("callout", 30),
                            ("faq", 35),
                            ("links", 39),
                            ("documents", 44),
                            ("testimonial", 47),
                            ("stats", 50),
                            ("cta", 52),
                            ("form_finder", 67),
                            ("conditions", 69),
                            ("visit_story", 77),
                            ("signs", 82),
                        ],
                        blank=True,
                        block_lookup={
                            0: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Small line above the heading.",
                                    "required": False,
                                },
                            ),
                            1: ("wagtail.blocks.CharBlock", (), {}),
                            2: ("wagtail.blocks.TextBlock", (), {"required": False}),
                            3: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {},
                            ),
                            4: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": [
                                        "h2",
                                        "h3",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ol",
                                        "ul",
                                        "document-link",
                                    ],
                                    "template": "core/blocks/paragraph.html",
                                },
                            ),
                            5: ("wagtail.blocks.CharBlock", (), {"required": False}),
                            6: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul", "ol"]},
                            ),
                            7: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            8: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blocks", "Building blocks"),
                                        ("garden", "Garden"),
                                        ("team", "Team circle"),
                                        ("gym", "Therapy gym"),
                                    ],
                                    "help_text": "Shown when no image is chosen.",
                                },
                            ),
                            9: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {"choices": [("right", "Right"), ("left", "Left")]},
                            ),
                            10: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            11: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "Or a web address", "required": False},
                            ),
                            12: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Optional. Jump to a section of the chosen page, e.g. does-this-sound-like-your-child.",
                                    "required": False,
                                },
                            ),
                            13: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {"required": False},
                            ),
                            14: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("eyebrow", 5),
                                        ("heading", 1),
                                        ("text", 6),
                                        ("image", 7),
                                        ("illustration", 8),
                                        ("image_side", 9),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            15: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                            16: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blob", "Soft blob"),
                                        ("rounded", "Rounded rectangle"),
                                    ]
                                },
                            ),
                            17: (
                                "wagtail.blocks.StructBlock",
                                [[("image", 15), ("caption", 5), ("shape", 16)]],
                                {},
                            ),
                            18: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {"required": False},
                            ),
                            19: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
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
                                },
                            ),
                            20: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("sun", "Sunny yellow"),
                                        ("coral", "Coral"),
                                        ("teal", "Teal"),
                                        ("sky", "Sky blue"),
                                        ("grape", "Grape"),
                                        ("leaf", "Leaf green"),
                                    ]
                                },
                            ),
                            21: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("icon", 19),
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("link", 13),
                                    ]
                                ],
                                {},
                            ),
                            22: ("wagtail.blocks.ListBlock", (21,), {}),
                            23: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("cards", 22)]],
                                {},
                            ),
                            24: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("text", 2), ("link", 13)]],
                                {},
                            ),
                            25: ("wagtail.blocks.ListBlock", (24,), {}),
                            26: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("steps", 25)]],
                                {},
                            ),
                            27: ("wagtail.blocks.ListBlock", (1,), {}),
                            28: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 5), ("color", 20), ("items", 27)]],
                                {},
                            ),
                            29: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "required": False,
                                },
                            ),
                            30: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("icon", 19),
                                        ("title", 1),
                                        ("text", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            31: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Common questions", "required": False},
                            ),
                            32: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul"]},
                            ),
                            33: (
                                "wagtail.blocks.StructBlock",
                                [[("question", 1), ("answer", 32)]],
                                {},
                            ),
                            34: ("wagtail.blocks.ListBlock", (33,), {}),
                            35: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 31), ("items", 34)]],
                                {},
                            ),
                            36: ("wagtail.blocks.URLBlock", (), {"required": False}),
                            37: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("url", 36), ("description", 5)]],
                                {},
                            ),
                            38: ("wagtail.blocks.ListBlock", (37,), {}),
                            39: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("links", 38)]],
                                {},
                            ),
                            40: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {"required": False},
                            ),
                            41: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'For newborns to 12 months'",
                                    "required": False,
                                },
                            ),
                            42: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("document", 40), ("note", 41)]],
                                {},
                            ),
                            43: ("wagtail.blocks.ListBlock", (42,), {}),
                            44: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("intro", 2), ("documents", 43)]],
                                {},
                            ),
                            45: ("wagtail.blocks.TextBlock", (), {}),
                            46: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"help_text": "e.g. 'Grace's mom'", "required": False},
                            ),
                            47: (
                                "wagtail.blocks.StructBlock",
                                [[("quote", 45), ("name", 1), ("role", 46)]],
                                {},
                            ),
                            48: (
                                "wagtail.blocks.StructBlock",
                                [[("number", 1), ("label", 1)]],
                                {},
                            ),
                            49: ("wagtail.blocks.ListBlock", (48,), {}),
                            50: ("wagtail.blocks.StructBlock", [[("stats", 49)]], {}),
                            51: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {},
                            ),
                            52: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("button", 51),
                                        ("secondary_button", 13),
                                    ]
                                ],
                                {},
                            ),
                            53: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "What brings you here today?"},
                            ),
                            54: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'My child is new to Beyond Limits'"
                                },
                            ),
                            55: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Asked when this path has options, e.g. 'Which service is your child starting?'",
                                    "required": False,
                                },
                            ),
                            56: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {
                                    "help_text": "Secure online form (e.g. LuxSci). Shown as 'Fill out online'.",
                                    "required": False,
                                },
                            ),
                            57: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {
                                    "help_text": "Printable PDF, if there is one.",
                                    "required": False,
                                },
                            ),
                            58: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'Only if you'll use telehealth'",
                                    "required": False,
                                },
                            ),
                            59: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("online_url", 56),
                                        ("document", 57),
                                        ("note", 58),
                                    ]
                                ],
                                {},
                            ),
                            60: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {"required": False},
                            ),
                            61: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 1), ("forms", 60), ("note", 29)]],
                                {},
                            ),
                            62: (
                                "wagtail.blocks.ListBlock",
                                (61,),
                                {
                                    "help_text": "Leave empty to go straight to the forms below.",
                                    "required": False,
                                },
                            ),
                            63: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {
                                    "help_text": "Forms for everyone on this path (added to any option's forms).",
                                    "required": False,
                                },
                            ),
                            64: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 54),
                                        ("description", 5),
                                        ("icon", 19),
                                        ("follow_up_question", 55),
                                        ("options", 62),
                                        ("forms", 63),
                                        ("note", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            65: ("wagtail.blocks.ListBlock", (64,), {}),
                            66: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "help_text": "How to send the forms back. Shown with every result.",
                                    "required": False,
                                },
                            ),
                            67: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("heading", 18),
                                        ("question", 53),
                                        ("paths", 65),
                                        ("return_note", 66),
                                    ]
                                ],
                                {},
                            ),
                            68: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Search for a concern", "required": False},
                            ),
                            69: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("filter_label", 68)]],
                                {},
                            ),
                            70: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Your first visit, one step at a time"},
                            ),
                            71: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "A short note for grown-ups at the top.",
                                    "required": False,
                                },
                            ),
                            72: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "A real photo of this spot, cropped to a 4:3 rectangle around the image's focal point. Until there is one, the icon is shown.",
                                    "required": False,
                                },
                            ),
                            73: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "One or two short sentences, written as the child: 'This is the front door.'"
                                },
                            ),
                            74: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Describe the photo for screen readers, e.g. 'Glass front door with the Beyond Limits sign above it.'",
                                    "required": False,
                                },
                            ),
                            75: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("photo", 72),
                                        ("icon", 19),
                                        ("text", 73),
                                        ("alt", 74),
                                    ]
                                ],
                                {"icon": "image"},
                            ),
                            76: ("wagtail.blocks.ListBlock", (75,), {}),
                            77: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 70), ("parent_note", 71), ("steps", 76)]],
                                {},
                            ),
                            78: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "default": "does-this-sound-like-your-child",
                                    "help_text": "Lets buttons jump straight to this section. Change it only if you also update those links.",
                                },
                            ),
                            79: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "One sign per line, in the words a parent would use."
                                },
                            ),
                            80: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("icon", 19),
                                        ("color", 20),
                                        ("signs", 79),
                                        ("link", 51),
                                    ]
                                ],
                                {"icon": "help"},
                            ),
                            81: ("wagtail.blocks.ListBlock", (80,), {}),
                            82: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("anchor", 78), ("cards", 81)]],
                                {},
                            ),
                        },
                    ),
                ),
                ("apply_email", models.EmailField(blank=True, max_length=254)),
                ("apply_url", models.URLField(blank=True)),
                ("is_open", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="ServiceIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "hero_intro",
                    models.TextField(
                        blank=True,
                        help_text="One or two friendly sentences under the page title.",
                    ),
                ),
                (
                    "hero_color",
                    models.CharField(
                        choices=[
                            ("indigo", "Soft indigo"),
                            ("sun", "Sunny yellow"),
                            ("coral", "Coral"),
                            ("teal", "Teal"),
                            ("sky", "Sky blue"),
                            ("grape", "Grape"),
                            ("leaf", "Leaf green"),
                            ("navy", "Navy (veterans)"),
                        ],
                        default="indigo",
                        max_length=10,
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", 3),
                            ("paragraph", 4),
                            ("split", 14),
                            ("image", 17),
                            ("cards", 23),
                            ("steps", 26),
                            ("checklist", 28),
                            ("callout", 30),
                            ("faq", 35),
                            ("links", 39),
                            ("documents", 44),
                            ("testimonial", 47),
                            ("stats", 50),
                            ("cta", 52),
                            ("form_finder", 67),
                            ("conditions", 69),
                            ("visit_story", 77),
                            ("signs", 82),
                        ],
                        blank=True,
                        block_lookup={
                            0: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Small line above the heading.",
                                    "required": False,
                                },
                            ),
                            1: ("wagtail.blocks.CharBlock", (), {}),
                            2: ("wagtail.blocks.TextBlock", (), {"required": False}),
                            3: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {},
                            ),
                            4: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": [
                                        "h2",
                                        "h3",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ol",
                                        "ul",
                                        "document-link",
                                    ],
                                    "template": "core/blocks/paragraph.html",
                                },
                            ),
                            5: ("wagtail.blocks.CharBlock", (), {"required": False}),
                            6: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul", "ol"]},
                            ),
                            7: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            8: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blocks", "Building blocks"),
                                        ("garden", "Garden"),
                                        ("team", "Team circle"),
                                        ("gym", "Therapy gym"),
                                    ],
                                    "help_text": "Shown when no image is chosen.",
                                },
                            ),
                            9: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {"choices": [("right", "Right"), ("left", "Left")]},
                            ),
                            10: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            11: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "Or a web address", "required": False},
                            ),
                            12: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Optional. Jump to a section of the chosen page, e.g. does-this-sound-like-your-child.",
                                    "required": False,
                                },
                            ),
                            13: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {"required": False},
                            ),
                            14: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("eyebrow", 5),
                                        ("heading", 1),
                                        ("text", 6),
                                        ("image", 7),
                                        ("illustration", 8),
                                        ("image_side", 9),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            15: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                            16: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blob", "Soft blob"),
                                        ("rounded", "Rounded rectangle"),
                                    ]
                                },
                            ),
                            17: (
                                "wagtail.blocks.StructBlock",
                                [[("image", 15), ("caption", 5), ("shape", 16)]],
                                {},
                            ),
                            18: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {"required": False},
                            ),
                            19: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
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
                                },
                            ),
                            20: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("sun", "Sunny yellow"),
                                        ("coral", "Coral"),
                                        ("teal", "Teal"),
                                        ("sky", "Sky blue"),
                                        ("grape", "Grape"),
                                        ("leaf", "Leaf green"),
                                    ]
                                },
                            ),
                            21: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("icon", 19),
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("link", 13),
                                    ]
                                ],
                                {},
                            ),
                            22: ("wagtail.blocks.ListBlock", (21,), {}),
                            23: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("cards", 22)]],
                                {},
                            ),
                            24: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("text", 2), ("link", 13)]],
                                {},
                            ),
                            25: ("wagtail.blocks.ListBlock", (24,), {}),
                            26: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("steps", 25)]],
                                {},
                            ),
                            27: ("wagtail.blocks.ListBlock", (1,), {}),
                            28: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 5), ("color", 20), ("items", 27)]],
                                {},
                            ),
                            29: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "required": False,
                                },
                            ),
                            30: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("icon", 19),
                                        ("title", 1),
                                        ("text", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            31: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Common questions", "required": False},
                            ),
                            32: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul"]},
                            ),
                            33: (
                                "wagtail.blocks.StructBlock",
                                [[("question", 1), ("answer", 32)]],
                                {},
                            ),
                            34: ("wagtail.blocks.ListBlock", (33,), {}),
                            35: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 31), ("items", 34)]],
                                {},
                            ),
                            36: ("wagtail.blocks.URLBlock", (), {"required": False}),
                            37: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("url", 36), ("description", 5)]],
                                {},
                            ),
                            38: ("wagtail.blocks.ListBlock", (37,), {}),
                            39: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("links", 38)]],
                                {},
                            ),
                            40: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {"required": False},
                            ),
                            41: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'For newborns to 12 months'",
                                    "required": False,
                                },
                            ),
                            42: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("document", 40), ("note", 41)]],
                                {},
                            ),
                            43: ("wagtail.blocks.ListBlock", (42,), {}),
                            44: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("intro", 2), ("documents", 43)]],
                                {},
                            ),
                            45: ("wagtail.blocks.TextBlock", (), {}),
                            46: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"help_text": "e.g. 'Grace's mom'", "required": False},
                            ),
                            47: (
                                "wagtail.blocks.StructBlock",
                                [[("quote", 45), ("name", 1), ("role", 46)]],
                                {},
                            ),
                            48: (
                                "wagtail.blocks.StructBlock",
                                [[("number", 1), ("label", 1)]],
                                {},
                            ),
                            49: ("wagtail.blocks.ListBlock", (48,), {}),
                            50: ("wagtail.blocks.StructBlock", [[("stats", 49)]], {}),
                            51: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {},
                            ),
                            52: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("button", 51),
                                        ("secondary_button", 13),
                                    ]
                                ],
                                {},
                            ),
                            53: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "What brings you here today?"},
                            ),
                            54: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'My child is new to Beyond Limits'"
                                },
                            ),
                            55: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Asked when this path has options, e.g. 'Which service is your child starting?'",
                                    "required": False,
                                },
                            ),
                            56: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {
                                    "help_text": "Secure online form (e.g. LuxSci). Shown as 'Fill out online'.",
                                    "required": False,
                                },
                            ),
                            57: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {
                                    "help_text": "Printable PDF, if there is one.",
                                    "required": False,
                                },
                            ),
                            58: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'Only if you'll use telehealth'",
                                    "required": False,
                                },
                            ),
                            59: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("online_url", 56),
                                        ("document", 57),
                                        ("note", 58),
                                    ]
                                ],
                                {},
                            ),
                            60: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {"required": False},
                            ),
                            61: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 1), ("forms", 60), ("note", 29)]],
                                {},
                            ),
                            62: (
                                "wagtail.blocks.ListBlock",
                                (61,),
                                {
                                    "help_text": "Leave empty to go straight to the forms below.",
                                    "required": False,
                                },
                            ),
                            63: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {
                                    "help_text": "Forms for everyone on this path (added to any option's forms).",
                                    "required": False,
                                },
                            ),
                            64: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 54),
                                        ("description", 5),
                                        ("icon", 19),
                                        ("follow_up_question", 55),
                                        ("options", 62),
                                        ("forms", 63),
                                        ("note", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            65: ("wagtail.blocks.ListBlock", (64,), {}),
                            66: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "help_text": "How to send the forms back. Shown with every result.",
                                    "required": False,
                                },
                            ),
                            67: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("heading", 18),
                                        ("question", 53),
                                        ("paths", 65),
                                        ("return_note", 66),
                                    ]
                                ],
                                {},
                            ),
                            68: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Search for a concern", "required": False},
                            ),
                            69: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("filter_label", 68)]],
                                {},
                            ),
                            70: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Your first visit, one step at a time"},
                            ),
                            71: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "A short note for grown-ups at the top.",
                                    "required": False,
                                },
                            ),
                            72: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "A real photo of this spot, cropped to a 4:3 rectangle around the image's focal point. Until there is one, the icon is shown.",
                                    "required": False,
                                },
                            ),
                            73: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "One or two short sentences, written as the child: 'This is the front door.'"
                                },
                            ),
                            74: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Describe the photo for screen readers, e.g. 'Glass front door with the Beyond Limits sign above it.'",
                                    "required": False,
                                },
                            ),
                            75: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("photo", 72),
                                        ("icon", 19),
                                        ("text", 73),
                                        ("alt", 74),
                                    ]
                                ],
                                {"icon": "image"},
                            ),
                            76: ("wagtail.blocks.ListBlock", (75,), {}),
                            77: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 70), ("parent_note", 71), ("steps", 76)]],
                                {},
                            ),
                            78: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "default": "does-this-sound-like-your-child",
                                    "help_text": "Lets buttons jump straight to this section. Change it only if you also update those links.",
                                },
                            ),
                            79: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "One sign per line, in the words a parent would use."
                                },
                            ),
                            80: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("icon", 19),
                                        ("color", 20),
                                        ("signs", 79),
                                        ("link", 51),
                                    ]
                                ],
                                {"icon": "help"},
                            ),
                            81: ("wagtail.blocks.ListBlock", (80,), {}),
                            82: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("anchor", 78), ("cards", 81)]],
                                {},
                            ),
                        },
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="StandardPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "hero_intro",
                    models.TextField(
                        blank=True,
                        help_text="One or two friendly sentences under the page title.",
                    ),
                ),
                (
                    "hero_color",
                    models.CharField(
                        choices=[
                            ("indigo", "Soft indigo"),
                            ("sun", "Sunny yellow"),
                            ("coral", "Coral"),
                            ("teal", "Teal"),
                            ("sky", "Sky blue"),
                            ("grape", "Grape"),
                            ("leaf", "Leaf green"),
                            ("navy", "Navy (veterans)"),
                        ],
                        default="indigo",
                        max_length=10,
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", 3),
                            ("paragraph", 4),
                            ("split", 14),
                            ("image", 17),
                            ("cards", 23),
                            ("steps", 26),
                            ("checklist", 28),
                            ("callout", 30),
                            ("faq", 35),
                            ("links", 39),
                            ("documents", 44),
                            ("testimonial", 47),
                            ("stats", 50),
                            ("cta", 52),
                            ("form_finder", 67),
                            ("conditions", 69),
                            ("visit_story", 77),
                            ("signs", 82),
                        ],
                        blank=True,
                        block_lookup={
                            0: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Small line above the heading.",
                                    "required": False,
                                },
                            ),
                            1: ("wagtail.blocks.CharBlock", (), {}),
                            2: ("wagtail.blocks.TextBlock", (), {"required": False}),
                            3: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {},
                            ),
                            4: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": [
                                        "h2",
                                        "h3",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ol",
                                        "ul",
                                        "document-link",
                                    ],
                                    "template": "core/blocks/paragraph.html",
                                },
                            ),
                            5: ("wagtail.blocks.CharBlock", (), {"required": False}),
                            6: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul", "ol"]},
                            ),
                            7: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            8: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blocks", "Building blocks"),
                                        ("garden", "Garden"),
                                        ("team", "Team circle"),
                                        ("gym", "Therapy gym"),
                                    ],
                                    "help_text": "Shown when no image is chosen.",
                                },
                            ),
                            9: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {"choices": [("right", "Right"), ("left", "Left")]},
                            ),
                            10: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            11: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "Or a web address", "required": False},
                            ),
                            12: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Optional. Jump to a section of the chosen page, e.g. does-this-sound-like-your-child.",
                                    "required": False,
                                },
                            ),
                            13: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {"required": False},
                            ),
                            14: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("eyebrow", 5),
                                        ("heading", 1),
                                        ("text", 6),
                                        ("image", 7),
                                        ("illustration", 8),
                                        ("image_side", 9),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            15: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                            16: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blob", "Soft blob"),
                                        ("rounded", "Rounded rectangle"),
                                    ]
                                },
                            ),
                            17: (
                                "wagtail.blocks.StructBlock",
                                [[("image", 15), ("caption", 5), ("shape", 16)]],
                                {},
                            ),
                            18: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {"required": False},
                            ),
                            19: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
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
                                },
                            ),
                            20: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("sun", "Sunny yellow"),
                                        ("coral", "Coral"),
                                        ("teal", "Teal"),
                                        ("sky", "Sky blue"),
                                        ("grape", "Grape"),
                                        ("leaf", "Leaf green"),
                                    ]
                                },
                            ),
                            21: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("icon", 19),
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("link", 13),
                                    ]
                                ],
                                {},
                            ),
                            22: ("wagtail.blocks.ListBlock", (21,), {}),
                            23: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("cards", 22)]],
                                {},
                            ),
                            24: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("text", 2), ("link", 13)]],
                                {},
                            ),
                            25: ("wagtail.blocks.ListBlock", (24,), {}),
                            26: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("steps", 25)]],
                                {},
                            ),
                            27: ("wagtail.blocks.ListBlock", (1,), {}),
                            28: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 5), ("color", 20), ("items", 27)]],
                                {},
                            ),
                            29: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "required": False,
                                },
                            ),
                            30: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("icon", 19),
                                        ("title", 1),
                                        ("text", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            31: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Common questions", "required": False},
                            ),
                            32: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul"]},
                            ),
                            33: (
                                "wagtail.blocks.StructBlock",
                                [[("question", 1), ("answer", 32)]],
                                {},
                            ),
                            34: ("wagtail.blocks.ListBlock", (33,), {}),
                            35: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 31), ("items", 34)]],
                                {},
                            ),
                            36: ("wagtail.blocks.URLBlock", (), {"required": False}),
                            37: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("url", 36), ("description", 5)]],
                                {},
                            ),
                            38: ("wagtail.blocks.ListBlock", (37,), {}),
                            39: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("links", 38)]],
                                {},
                            ),
                            40: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {"required": False},
                            ),
                            41: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'For newborns to 12 months'",
                                    "required": False,
                                },
                            ),
                            42: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("document", 40), ("note", 41)]],
                                {},
                            ),
                            43: ("wagtail.blocks.ListBlock", (42,), {}),
                            44: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("intro", 2), ("documents", 43)]],
                                {},
                            ),
                            45: ("wagtail.blocks.TextBlock", (), {}),
                            46: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"help_text": "e.g. 'Grace's mom'", "required": False},
                            ),
                            47: (
                                "wagtail.blocks.StructBlock",
                                [[("quote", 45), ("name", 1), ("role", 46)]],
                                {},
                            ),
                            48: (
                                "wagtail.blocks.StructBlock",
                                [[("number", 1), ("label", 1)]],
                                {},
                            ),
                            49: ("wagtail.blocks.ListBlock", (48,), {}),
                            50: ("wagtail.blocks.StructBlock", [[("stats", 49)]], {}),
                            51: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {},
                            ),
                            52: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("button", 51),
                                        ("secondary_button", 13),
                                    ]
                                ],
                                {},
                            ),
                            53: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "What brings you here today?"},
                            ),
                            54: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'My child is new to Beyond Limits'"
                                },
                            ),
                            55: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Asked when this path has options, e.g. 'Which service is your child starting?'",
                                    "required": False,
                                },
                            ),
                            56: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {
                                    "help_text": "Secure online form (e.g. LuxSci). Shown as 'Fill out online'.",
                                    "required": False,
                                },
                            ),
                            57: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {
                                    "help_text": "Printable PDF, if there is one.",
                                    "required": False,
                                },
                            ),
                            58: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'Only if you'll use telehealth'",
                                    "required": False,
                                },
                            ),
                            59: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("online_url", 56),
                                        ("document", 57),
                                        ("note", 58),
                                    ]
                                ],
                                {},
                            ),
                            60: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {"required": False},
                            ),
                            61: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 1), ("forms", 60), ("note", 29)]],
                                {},
                            ),
                            62: (
                                "wagtail.blocks.ListBlock",
                                (61,),
                                {
                                    "help_text": "Leave empty to go straight to the forms below.",
                                    "required": False,
                                },
                            ),
                            63: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {
                                    "help_text": "Forms for everyone on this path (added to any option's forms).",
                                    "required": False,
                                },
                            ),
                            64: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 54),
                                        ("description", 5),
                                        ("icon", 19),
                                        ("follow_up_question", 55),
                                        ("options", 62),
                                        ("forms", 63),
                                        ("note", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            65: ("wagtail.blocks.ListBlock", (64,), {}),
                            66: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "help_text": "How to send the forms back. Shown with every result.",
                                    "required": False,
                                },
                            ),
                            67: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("heading", 18),
                                        ("question", 53),
                                        ("paths", 65),
                                        ("return_note", 66),
                                    ]
                                ],
                                {},
                            ),
                            68: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Search for a concern", "required": False},
                            ),
                            69: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("filter_label", 68)]],
                                {},
                            ),
                            70: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Your first visit, one step at a time"},
                            ),
                            71: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "A short note for grown-ups at the top.",
                                    "required": False,
                                },
                            ),
                            72: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "A real photo of this spot, cropped to a 4:3 rectangle around the image's focal point. Until there is one, the icon is shown.",
                                    "required": False,
                                },
                            ),
                            73: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "One or two short sentences, written as the child: 'This is the front door.'"
                                },
                            ),
                            74: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Describe the photo for screen readers, e.g. 'Glass front door with the Beyond Limits sign above it.'",
                                    "required": False,
                                },
                            ),
                            75: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("photo", 72),
                                        ("icon", 19),
                                        ("text", 73),
                                        ("alt", 74),
                                    ]
                                ],
                                {"icon": "image"},
                            ),
                            76: ("wagtail.blocks.ListBlock", (75,), {}),
                            77: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 70), ("parent_note", 71), ("steps", 76)]],
                                {},
                            ),
                            78: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "default": "does-this-sound-like-your-child",
                                    "help_text": "Lets buttons jump straight to this section. Change it only if you also update those links.",
                                },
                            ),
                            79: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "One sign per line, in the words a parent would use."
                                },
                            ),
                            80: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("icon", 19),
                                        ("color", 20),
                                        ("signs", 79),
                                        ("link", 51),
                                    ]
                                ],
                                {"icon": "help"},
                            ),
                            81: ("wagtail.blocks.ListBlock", (80,), {}),
                            82: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("anchor", 78), ("cards", 81)]],
                                {},
                            ),
                        },
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="ContactFormField",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "clean_name",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Safe name of the form field, the label converted to ascii_snake_case",
                        max_length=255,
                        verbose_name="name",
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        help_text="The label of the form field",
                        max_length=255,
                        verbose_name="label",
                    ),
                ),
                (
                    "field_type",
                    models.CharField(
                        choices=[
                            ("singleline", "Single line text"),
                            ("multiline", "Multi-line text"),
                            ("email", "Email"),
                            ("number", "Number"),
                            ("url", "URL"),
                            ("checkbox", "Checkbox"),
                            ("checkboxes", "Checkboxes"),
                            ("dropdown", "Drop down"),
                            ("multiselect", "Multiple select"),
                            ("radio", "Radio buttons"),
                            ("date", "Date"),
                            ("datetime", "Date/time"),
                            ("hidden", "Hidden field"),
                        ],
                        max_length=16,
                        verbose_name="field type",
                    ),
                ),
                (
                    "required",
                    models.BooleanField(default=True, verbose_name="required"),
                ),
                (
                    "choices",
                    models.TextField(
                        blank=True,
                        help_text="Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.",
                        verbose_name="choices",
                    ),
                ),
                (
                    "default_value",
                    models.TextField(
                        blank=True,
                        help_text="Default value. Comma or new line separated values supported for checkboxes.",
                        verbose_name="default value",
                    ),
                ),
                (
                    "help_text",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="help text"
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="form_fields",
                        to="pages.contactpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ServicePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "hero_intro",
                    models.TextField(
                        blank=True,
                        help_text="One or two friendly sentences under the page title.",
                    ),
                ),
                (
                    "hero_color",
                    models.CharField(
                        choices=[
                            ("indigo", "Soft indigo"),
                            ("sun", "Sunny yellow"),
                            ("coral", "Coral"),
                            ("teal", "Teal"),
                            ("sky", "Sky blue"),
                            ("grape", "Grape"),
                            ("leaf", "Leaf green"),
                            ("navy", "Navy (veterans)"),
                        ],
                        default="indigo",
                        max_length=10,
                    ),
                ),
                (
                    "short_name",
                    models.CharField(blank=True, help_text="e.g. 'OT'", max_length=40),
                ),
                (
                    "icon",
                    models.CharField(
                        choices=[
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
                        ],
                        default="star",
                        max_length=20,
                    ),
                ),
                (
                    "summary",
                    models.TextField(
                        help_text="One or two sentences for cards and listings."
                    ),
                ),
                (
                    "age_range",
                    models.CharField(blank=True, default="Birth to 21", max_length=60),
                ),
                (
                    "show_in_overview",
                    models.BooleanField(
                        default=True, help_text="Show on the home page services list."
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
                (
                    "helps_with",
                    models.TextField(
                        blank=True,
                        help_text="One item per line. Conditions and needs this service helps with.",
                    ),
                ),
                (
                    "what_we_offer",
                    models.TextField(blank=True, help_text="One item per line."),
                ),
                (
                    "first_visit",
                    models.TextField(
                        blank=True, help_text="What to expect at the first visit."
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", 3),
                            ("paragraph", 4),
                            ("split", 14),
                            ("image", 17),
                            ("cards", 23),
                            ("steps", 26),
                            ("checklist", 28),
                            ("callout", 30),
                            ("faq", 35),
                            ("links", 39),
                            ("documents", 44),
                            ("testimonial", 47),
                            ("stats", 50),
                            ("cta", 52),
                            ("form_finder", 67),
                            ("conditions", 69),
                            ("visit_story", 77),
                            ("signs", 82),
                        ],
                        blank=True,
                        block_lookup={
                            0: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Small line above the heading.",
                                    "required": False,
                                },
                            ),
                            1: ("wagtail.blocks.CharBlock", (), {}),
                            2: ("wagtail.blocks.TextBlock", (), {"required": False}),
                            3: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {},
                            ),
                            4: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": [
                                        "h2",
                                        "h3",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ol",
                                        "ul",
                                        "document-link",
                                    ],
                                    "template": "core/blocks/paragraph.html",
                                },
                            ),
                            5: ("wagtail.blocks.CharBlock", (), {"required": False}),
                            6: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul", "ol"]},
                            ),
                            7: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            8: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blocks", "Building blocks"),
                                        ("garden", "Garden"),
                                        ("team", "Team circle"),
                                        ("gym", "Therapy gym"),
                                    ],
                                    "help_text": "Shown when no image is chosen.",
                                },
                            ),
                            9: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {"choices": [("right", "Right"), ("left", "Left")]},
                            ),
                            10: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            11: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "Or a web address", "required": False},
                            ),
                            12: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Optional. Jump to a section of the chosen page, e.g. does-this-sound-like-your-child.",
                                    "required": False,
                                },
                            ),
                            13: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {"required": False},
                            ),
                            14: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("eyebrow", 5),
                                        ("heading", 1),
                                        ("text", 6),
                                        ("image", 7),
                                        ("illustration", 8),
                                        ("image_side", 9),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            15: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                            16: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blob", "Soft blob"),
                                        ("rounded", "Rounded rectangle"),
                                    ]
                                },
                            ),
                            17: (
                                "wagtail.blocks.StructBlock",
                                [[("image", 15), ("caption", 5), ("shape", 16)]],
                                {},
                            ),
                            18: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {"required": False},
                            ),
                            19: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
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
                                },
                            ),
                            20: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("sun", "Sunny yellow"),
                                        ("coral", "Coral"),
                                        ("teal", "Teal"),
                                        ("sky", "Sky blue"),
                                        ("grape", "Grape"),
                                        ("leaf", "Leaf green"),
                                    ]
                                },
                            ),
                            21: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("icon", 19),
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("link", 13),
                                    ]
                                ],
                                {},
                            ),
                            22: ("wagtail.blocks.ListBlock", (21,), {}),
                            23: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("cards", 22)]],
                                {},
                            ),
                            24: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("text", 2), ("link", 13)]],
                                {},
                            ),
                            25: ("wagtail.blocks.ListBlock", (24,), {}),
                            26: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("steps", 25)]],
                                {},
                            ),
                            27: ("wagtail.blocks.ListBlock", (1,), {}),
                            28: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 5), ("color", 20), ("items", 27)]],
                                {},
                            ),
                            29: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "required": False,
                                },
                            ),
                            30: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("icon", 19),
                                        ("title", 1),
                                        ("text", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            31: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Common questions", "required": False},
                            ),
                            32: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul"]},
                            ),
                            33: (
                                "wagtail.blocks.StructBlock",
                                [[("question", 1), ("answer", 32)]],
                                {},
                            ),
                            34: ("wagtail.blocks.ListBlock", (33,), {}),
                            35: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 31), ("items", 34)]],
                                {},
                            ),
                            36: ("wagtail.blocks.URLBlock", (), {"required": False}),
                            37: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("url", 36), ("description", 5)]],
                                {},
                            ),
                            38: ("wagtail.blocks.ListBlock", (37,), {}),
                            39: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("links", 38)]],
                                {},
                            ),
                            40: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {"required": False},
                            ),
                            41: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'For newborns to 12 months'",
                                    "required": False,
                                },
                            ),
                            42: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("document", 40), ("note", 41)]],
                                {},
                            ),
                            43: ("wagtail.blocks.ListBlock", (42,), {}),
                            44: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("intro", 2), ("documents", 43)]],
                                {},
                            ),
                            45: ("wagtail.blocks.TextBlock", (), {}),
                            46: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"help_text": "e.g. 'Grace's mom'", "required": False},
                            ),
                            47: (
                                "wagtail.blocks.StructBlock",
                                [[("quote", 45), ("name", 1), ("role", 46)]],
                                {},
                            ),
                            48: (
                                "wagtail.blocks.StructBlock",
                                [[("number", 1), ("label", 1)]],
                                {},
                            ),
                            49: ("wagtail.blocks.ListBlock", (48,), {}),
                            50: ("wagtail.blocks.StructBlock", [[("stats", 49)]], {}),
                            51: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {},
                            ),
                            52: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("button", 51),
                                        ("secondary_button", 13),
                                    ]
                                ],
                                {},
                            ),
                            53: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "What brings you here today?"},
                            ),
                            54: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'My child is new to Beyond Limits'"
                                },
                            ),
                            55: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Asked when this path has options, e.g. 'Which service is your child starting?'",
                                    "required": False,
                                },
                            ),
                            56: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {
                                    "help_text": "Secure online form (e.g. LuxSci). Shown as 'Fill out online'.",
                                    "required": False,
                                },
                            ),
                            57: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {
                                    "help_text": "Printable PDF, if there is one.",
                                    "required": False,
                                },
                            ),
                            58: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'Only if you'll use telehealth'",
                                    "required": False,
                                },
                            ),
                            59: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("online_url", 56),
                                        ("document", 57),
                                        ("note", 58),
                                    ]
                                ],
                                {},
                            ),
                            60: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {"required": False},
                            ),
                            61: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 1), ("forms", 60), ("note", 29)]],
                                {},
                            ),
                            62: (
                                "wagtail.blocks.ListBlock",
                                (61,),
                                {
                                    "help_text": "Leave empty to go straight to the forms below.",
                                    "required": False,
                                },
                            ),
                            63: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {
                                    "help_text": "Forms for everyone on this path (added to any option's forms).",
                                    "required": False,
                                },
                            ),
                            64: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 54),
                                        ("description", 5),
                                        ("icon", 19),
                                        ("follow_up_question", 55),
                                        ("options", 62),
                                        ("forms", 63),
                                        ("note", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            65: ("wagtail.blocks.ListBlock", (64,), {}),
                            66: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "help_text": "How to send the forms back. Shown with every result.",
                                    "required": False,
                                },
                            ),
                            67: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("heading", 18),
                                        ("question", 53),
                                        ("paths", 65),
                                        ("return_note", 66),
                                    ]
                                ],
                                {},
                            ),
                            68: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Search for a concern", "required": False},
                            ),
                            69: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("filter_label", 68)]],
                                {},
                            ),
                            70: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Your first visit, one step at a time"},
                            ),
                            71: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "A short note for grown-ups at the top.",
                                    "required": False,
                                },
                            ),
                            72: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "A real photo of this spot, cropped to a 4:3 rectangle around the image's focal point. Until there is one, the icon is shown.",
                                    "required": False,
                                },
                            ),
                            73: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "One or two short sentences, written as the child: 'This is the front door.'"
                                },
                            ),
                            74: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Describe the photo for screen readers, e.g. 'Glass front door with the Beyond Limits sign above it.'",
                                    "required": False,
                                },
                            ),
                            75: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("photo", 72),
                                        ("icon", 19),
                                        ("text", 73),
                                        ("alt", 74),
                                    ]
                                ],
                                {"icon": "image"},
                            ),
                            76: ("wagtail.blocks.ListBlock", (75,), {}),
                            77: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 70), ("parent_note", 71), ("steps", 76)]],
                                {},
                            ),
                            78: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "default": "does-this-sound-like-your-child",
                                    "help_text": "Lets buttons jump straight to this section. Change it only if you also update those links.",
                                },
                            ),
                            79: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "One sign per line, in the words a parent would use."
                                },
                            ),
                            80: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("icon", 19),
                                        ("color", 20),
                                        ("signs", 79),
                                        ("link", 51),
                                    ]
                                ],
                                {"icon": "help"},
                            ),
                            81: ("wagtail.blocks.ListBlock", (80,), {}),
                            82: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("anchor", 78), ("cards", 81)]],
                                {},
                            ),
                        },
                    ),
                ),
                (
                    "photo",
                    models.ForeignKey(
                        blank=True,
                        help_text="One photo of this therapy, shown beside 'Your first visit'. It's cropped square around the image's focal point, so set the focal point on the image if faces get cut off. A real photo of your team at work is best.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        help_text="Used in the profile address. Filled in from the name if left blank.",
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "credentials",
                    models.CharField(
                        blank=True, help_text="e.g. 'M.S., CCC-SLP'", max_length=80
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="e.g. 'Clinical Coordinator'",
                        max_length=100,
                    ),
                ),
                (
                    "discipline",
                    models.CharField(
                        choices=[
                            ("audiology", "Audiology"),
                            ("ot", "Occupational Therapy"),
                            ("pt", "Physical Therapy"),
                            ("slp", "Speech-Language Pathology"),
                            ("office", "Front Office & Leadership"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, help_text="One or two sentences for the team card."
                    ),
                ),
                (
                    "intro",
                    models.CharField(
                        blank=True,
                        help_text="Opening line on the profile, e.g. 'Meet Kimberly!'",
                        max_length=200,
                    ),
                ),
                (
                    "licensure",
                    models.TextField(
                        blank=True,
                        help_text="Licenses and certifications, one per line.",
                    ),
                ),
                (
                    "education",
                    models.TextField(blank=True, help_text="Degrees, one per line."),
                ),
                (
                    "experience",
                    wagtail.fields.RichTextField(
                        blank=True, help_text="Clinical experience and interests."
                    ),
                ),
                (
                    "favorite_thing",
                    models.CharField(
                        blank=True,
                        help_text="A fun line families and future teammates will remember.",
                        max_length=140,
                    ),
                ),
                (
                    "is_clinician",
                    models.BooleanField(
                        default=True,
                        help_text="Untick for front office staff. Only clinicians appear in the home page team row.",
                    ),
                ),
                ("sort_order", models.IntegerField(default=0)),
                (
                    "photo",
                    models.ForeignKey(
                        blank=True,
                        help_text="Cropped square around the image's focal point. A head-and-shoulders photo works best.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "provider",
                "ordering": ["sort_order", "name"],
            },
            bases=(modelsearch.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name="TeamPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "hero_intro",
                    models.TextField(
                        blank=True,
                        help_text="One or two friendly sentences under the page title.",
                    ),
                ),
                (
                    "hero_color",
                    models.CharField(
                        choices=[
                            ("indigo", "Soft indigo"),
                            ("sun", "Sunny yellow"),
                            ("coral", "Coral"),
                            ("teal", "Teal"),
                            ("sky", "Sky blue"),
                            ("grape", "Grape"),
                            ("leaf", "Leaf green"),
                            ("navy", "Navy (veterans)"),
                        ],
                        default="indigo",
                        max_length=10,
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", 3),
                            ("paragraph", 4),
                            ("split", 14),
                            ("image", 17),
                            ("cards", 23),
                            ("steps", 26),
                            ("checklist", 28),
                            ("callout", 30),
                            ("faq", 35),
                            ("links", 39),
                            ("documents", 44),
                            ("testimonial", 47),
                            ("stats", 50),
                            ("cta", 52),
                            ("form_finder", 67),
                            ("conditions", 69),
                            ("visit_story", 77),
                            ("signs", 82),
                        ],
                        blank=True,
                        block_lookup={
                            0: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Small line above the heading.",
                                    "required": False,
                                },
                            ),
                            1: ("wagtail.blocks.CharBlock", (), {}),
                            2: ("wagtail.blocks.TextBlock", (), {"required": False}),
                            3: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {},
                            ),
                            4: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": [
                                        "h2",
                                        "h3",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ol",
                                        "ul",
                                        "document-link",
                                    ],
                                    "template": "core/blocks/paragraph.html",
                                },
                            ),
                            5: ("wagtail.blocks.CharBlock", (), {"required": False}),
                            6: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul", "ol"]},
                            ),
                            7: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            8: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blocks", "Building blocks"),
                                        ("garden", "Garden"),
                                        ("team", "Team circle"),
                                        ("gym", "Therapy gym"),
                                    ],
                                    "help_text": "Shown when no image is chosen.",
                                },
                            ),
                            9: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {"choices": [("right", "Right"), ("left", "Left")]},
                            ),
                            10: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            11: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "Or a web address", "required": False},
                            ),
                            12: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Optional. Jump to a section of the chosen page, e.g. does-this-sound-like-your-child.",
                                    "required": False,
                                },
                            ),
                            13: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {"required": False},
                            ),
                            14: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("eyebrow", 5),
                                        ("heading", 1),
                                        ("text", 6),
                                        ("image", 7),
                                        ("illustration", 8),
                                        ("image_side", 9),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            15: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                            16: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("blob", "Soft blob"),
                                        ("rounded", "Rounded rectangle"),
                                    ]
                                },
                            ),
                            17: (
                                "wagtail.blocks.StructBlock",
                                [[("image", 15), ("caption", 5), ("shape", 16)]],
                                {},
                            ),
                            18: (
                                "wagtail.blocks.StructBlock",
                                [[("eyebrow", 0), ("heading", 1), ("intro", 2)]],
                                {"required": False},
                            ),
                            19: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
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
                                },
                            ),
                            20: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("sun", "Sunny yellow"),
                                        ("coral", "Coral"),
                                        ("teal", "Teal"),
                                        ("sky", "Sky blue"),
                                        ("grape", "Grape"),
                                        ("leaf", "Leaf green"),
                                    ]
                                },
                            ),
                            21: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("icon", 19),
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("link", 13),
                                    ]
                                ],
                                {},
                            ),
                            22: ("wagtail.blocks.ListBlock", (21,), {}),
                            23: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("cards", 22)]],
                                {},
                            ),
                            24: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("text", 2), ("link", 13)]],
                                {},
                            ),
                            25: ("wagtail.blocks.ListBlock", (24,), {}),
                            26: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 18), ("steps", 25)]],
                                {},
                            ),
                            27: ("wagtail.blocks.ListBlock", (1,), {}),
                            28: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 5), ("color", 20), ("items", 27)]],
                                {},
                            ),
                            29: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "required": False,
                                },
                            ),
                            30: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("icon", 19),
                                        ("title", 1),
                                        ("text", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            31: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Common questions", "required": False},
                            ),
                            32: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic", "link", "ul"]},
                            ),
                            33: (
                                "wagtail.blocks.StructBlock",
                                [[("question", 1), ("answer", 32)]],
                                {},
                            ),
                            34: ("wagtail.blocks.ListBlock", (33,), {}),
                            35: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 31), ("items", 34)]],
                                {},
                            ),
                            36: ("wagtail.blocks.URLBlock", (), {"required": False}),
                            37: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("url", 36), ("description", 5)]],
                                {},
                            ),
                            38: ("wagtail.blocks.ListBlock", (37,), {}),
                            39: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("links", 38)]],
                                {},
                            ),
                            40: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {"required": False},
                            ),
                            41: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'For newborns to 12 months'",
                                    "required": False,
                                },
                            ),
                            42: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("document", 40), ("note", 41)]],
                                {},
                            ),
                            43: ("wagtail.blocks.ListBlock", (42,), {}),
                            44: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 1), ("intro", 2), ("documents", 43)]],
                                {},
                            ),
                            45: ("wagtail.blocks.TextBlock", (), {}),
                            46: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"help_text": "e.g. 'Grace's mom'", "required": False},
                            ),
                            47: (
                                "wagtail.blocks.StructBlock",
                                [[("quote", 45), ("name", 1), ("role", 46)]],
                                {},
                            ),
                            48: (
                                "wagtail.blocks.StructBlock",
                                [[("number", 1), ("label", 1)]],
                                {},
                            ),
                            49: ("wagtail.blocks.ListBlock", (48,), {}),
                            50: ("wagtail.blocks.StructBlock", [[("stats", 49)]], {}),
                            51: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 5),
                                        ("page", 10),
                                        ("external_url", 11),
                                        ("anchor", 12),
                                    ]
                                ],
                                {},
                            ),
                            52: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("color", 20),
                                        ("title", 1),
                                        ("text", 2),
                                        ("button", 51),
                                        ("secondary_button", 13),
                                    ]
                                ],
                                {},
                            ),
                            53: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "What brings you here today?"},
                            ),
                            54: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'My child is new to Beyond Limits'"
                                },
                            ),
                            55: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Asked when this path has options, e.g. 'Which service is your child starting?'",
                                    "required": False,
                                },
                            ),
                            56: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {
                                    "help_text": "Secure online form (e.g. LuxSci). Shown as 'Fill out online'.",
                                    "required": False,
                                },
                            ),
                            57: (
                                "wagtail.documents.blocks.DocumentChooserBlock",
                                (),
                                {
                                    "help_text": "Printable PDF, if there is one.",
                                    "required": False,
                                },
                            ),
                            58: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "e.g. 'Only if you'll use telehealth'",
                                    "required": False,
                                },
                            ),
                            59: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("online_url", 56),
                                        ("document", 57),
                                        ("note", 58),
                                    ]
                                ],
                                {},
                            ),
                            60: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {"required": False},
                            ),
                            61: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 1), ("forms", 60), ("note", 29)]],
                                {},
                            ),
                            62: (
                                "wagtail.blocks.ListBlock",
                                (61,),
                                {
                                    "help_text": "Leave empty to go straight to the forms below.",
                                    "required": False,
                                },
                            ),
                            63: (
                                "wagtail.blocks.ListBlock",
                                (59,),
                                {
                                    "help_text": "Forms for everyone on this path (added to any option's forms).",
                                    "required": False,
                                },
                            ),
                            64: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 54),
                                        ("description", 5),
                                        ("icon", 19),
                                        ("follow_up_question", 55),
                                        ("options", 62),
                                        ("forms", 63),
                                        ("note", 29),
                                        ("button", 13),
                                    ]
                                ],
                                {},
                            ),
                            65: ("wagtail.blocks.ListBlock", (64,), {}),
                            66: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": ["bold", "italic", "link"],
                                    "help_text": "How to send the forms back. Shown with every result.",
                                    "required": False,
                                },
                            ),
                            67: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("heading", 18),
                                        ("question", 53),
                                        ("paths", 65),
                                        ("return_note", 66),
                                    ]
                                ],
                                {},
                            ),
                            68: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Search for a concern", "required": False},
                            ),
                            69: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("filter_label", 68)]],
                                {},
                            ),
                            70: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Your first visit, one step at a time"},
                            ),
                            71: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "A short note for grown-ups at the top.",
                                    "required": False,
                                },
                            ),
                            72: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "A real photo of this spot, cropped to a 4:3 rectangle around the image's focal point. Until there is one, the icon is shown.",
                                    "required": False,
                                },
                            ),
                            73: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "One or two short sentences, written as the child: 'This is the front door.'"
                                },
                            ),
                            74: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Describe the photo for screen readers, e.g. 'Glass front door with the Beyond Limits sign above it.'",
                                    "required": False,
                                },
                            ),
                            75: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("photo", 72),
                                        ("icon", 19),
                                        ("text", 73),
                                        ("alt", 74),
                                    ]
                                ],
                                {"icon": "image"},
                            ),
                            76: ("wagtail.blocks.ListBlock", (75,), {}),
                            77: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 70), ("parent_note", 71), ("steps", 76)]],
                                {},
                            ),
                            78: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "default": "does-this-sound-like-your-child",
                                    "help_text": "Lets buttons jump straight to this section. Change it only if you also update those links.",
                                },
                            ),
                            79: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "help_text": "One sign per line, in the words a parent would use."
                                },
                            ),
                            80: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("title", 1),
                                        ("icon", 19),
                                        ("color", 20),
                                        ("signs", 79),
                                        ("link", 51),
                                    ]
                                ],
                                {"icon": "help"},
                            ),
                            81: ("wagtail.blocks.ListBlock", (80,), {}),
                            82: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("anchor", 78), ("cards", 81)]],
                                {},
                            ),
                        },
                    ),
                ),
                (
                    "group_photo",
                    models.ForeignKey(
                        blank=True,
                        help_text="A photo of the whole team, shown above the providers. Any shape works: the whole photo is shown, never cropped. Wider than tall, at least 1600 pixels across, looks best. Fill in the image's Description for screen readers. Until there is one, an illustration is shown.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
                models.Model,
            ),
        ),
    ]
