
import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    # Replaces the original migration history, which databases created
    # before this squash have already applied.
    replaces = [("home", "0001_initial"), ("home", "0002_alter_homepage_body"), ("home", "0003_alter_homepage_body"), ("home", "0004_alter_homepage_body"), ("home", "0005_alter_homepage_body_alter_homepage_slides"), ("home", "0006_alter_homepage_body_alter_homepage_slides"), ("home", "0007_alter_homepage_body")]

    initial = True

    dependencies = [
        ("wagtailcore", "0097_baselogentry_uuid_action_timestamp_indexes"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
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
                    "slides",
                    wagtail.fields.StreamField(
                        [("slide", 12)],
                        blank=True,
                        block_lookup={
                            0: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "Shown in the round-topped frame on the right, cropped square around the focal point. Without one, the illustration below is shown.",
                                    "required": False,
                                },
                            ),
                            1: (
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
                                        ("indigo", "Soft indigo"),
                                    ]
                                },
                            ),
                            2: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("hero", "Rainbow and blocks"),
                                        ("blocks", "Building blocks"),
                                        ("garden", "Garden"),
                                        ("team", "Team circle"),
                                        ("gym", "Therapy gym"),
                                    ],
                                    "help_text": "Used when no photo is chosen.",
                                },
                            ),
                            3: (
                                "wagtail.blocks.ChoiceBlock",
                                [],
                                {
                                    "choices": [
                                        ("indigo", "Indigo"),
                                        ("teal", "Green"),
                                        ("coral", "Red"),
                                        ("grape", "Grape"),
                                        ("sky", "Blue"),
                                        ("navy", "Navy"),
                                    ]
                                },
                            ),
                            4: ("wagtail.blocks.CharBlock", (), {"required": False}),
                            5: ("wagtail.blocks.CharBlock", (), {}),
                            6: ("wagtail.blocks.TextBlock", (), {"required": False}),
                            7: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            8: (
                                "wagtail.blocks.URLBlock",
                                (),
                                {"label": "Or a web address", "required": False},
                            ),
                            9: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Optional. Jump to a section of the chosen page, e.g. does-this-sound-like-your-child.",
                                    "required": False,
                                },
                            ),
                            10: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("label", 4),
                                        ("page", 7),
                                        ("external_url", 8),
                                        ("anchor", 9),
                                    ]
                                ],
                                {"required": False},
                            ),
                            11: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Small line under the button.",
                                    "required": False,
                                },
                            ),
                            12: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("image", 0),
                                        ("background", 1),
                                        ("illustration", 2),
                                        ("box_color", 3),
                                        ("eyebrow", 4),
                                        ("title", 5),
                                        ("text", 6),
                                        ("button", 10),
                                        ("note", 11),
                                    ]
                                ],
                                {},
                            ),
                        },
                        help_text="The rotating banner at the top. One slide shows without rotating.",
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
                            ("quick_links", 85),
                            ("services_overview", 86),
                            ("team_teaser", 88),
                            ("careers_band", 91),
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
                            83: (
                                "wagtail.blocks.StructBlock",
                                [[("title", 1), ("text", 5), ("link", 51)]],
                                {},
                            ),
                            84: ("wagtail.blocks.ListBlock", (83,), {"max_num": 4}),
                            85: ("wagtail.blocks.StructBlock", [[("links", 84)]], {}),
                            86: ("wagtail.blocks.StructBlock", [[("heading", 3)]], {}),
                            87: (
                                "wagtail.blocks.IntegerBlock",
                                (),
                                {"default": 8, "max_value": 16, "min_value": 3},
                            ),
                            88: (
                                "wagtail.blocks.StructBlock",
                                [[("heading", 3), ("count", 87), ("button", 13)]],
                                {},
                            ),
                            89: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {"default": "Work with us", "required": False},
                            ),
                            90: ("wagtail.blocks.ListBlock", (1,), {"required": False}),
                            91: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("eyebrow", 89),
                                        ("heading", 1),
                                        ("text", 2),
                                        ("points", 90),
                                        ("button", 51),
                                        ("image", 7),
                                    ]
                                ],
                                {},
                            ),
                        },
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
