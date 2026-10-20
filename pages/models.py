"""Page types for every page except the home page, plus TeamMember (providers).

See docs/ARCHITECTURE.md for how they fit together.
"""

from django.db import models
from django.http import Http404, HttpResponseNotAllowed
from django.template.response import TemplateResponse
from django.utils.text import slugify

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, FieldRowPanel, HelpPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from core.blocks import COLOR_CHOICES, ICON_CHOICES, BodyStreamBlock

HERO_COLOR_CHOICES = [("indigo", "Soft indigo")] + COLOR_CHOICES + [("navy", "Navy (veterans)")]


class HeroMixin(models.Model):
    """The colored title band at the top of every inner page (includes/page_hero.html)."""

    hero_intro = models.TextField(blank=True, help_text="One or two friendly sentences under the page title.")
    hero_color = models.CharField(max_length=10, choices=HERO_COLOR_CHOICES, default="indigo")

    hero_panels = [MultiFieldPanel([FieldPanel("hero_intro"), FieldPanel("hero_color")], "Page header")]

    class Meta:
        abstract = True


class StandardPage(HeroMixin, Page):
    """A general content page built from blocks: About, Get Started, Resources, Veterans, etc."""

    body = StreamField(BodyStreamBlock(), blank=True)

    content_panels = Page.content_panels + HeroMixin.hero_panels + [FieldPanel("body")]
    search_fields = Page.search_fields + [index.SearchField("hero_intro"), index.SearchField("body")]


class ServiceIndexPage(HeroMixin, Page):
    """The Services page. Lists its ServicePage children as cards above the body."""

    body = StreamField(BodyStreamBlock(), blank=True)

    content_panels = Page.content_panels + HeroMixin.hero_panels + [FieldPanel("body")]
    subpage_types = ["pages.ServicePage", "pages.StandardPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["services"] = ServicePage.objects.child_of(self).live().public()
        return context


class ServicePage(HeroMixin, Page):
    """One therapy (audiology, OT, PT, speech).

    The structured fields feed this page and every card that lists services
    (Services page, home page overview, sibling links). The multi-line text
    fields hold one item per line; templates split them with |split_lines.
    """

    short_name = models.CharField(max_length=40, blank=True, help_text="e.g. 'OT'")
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default="star")
    summary = models.TextField(help_text="One or two sentences for cards and listings.")
    age_range = models.CharField(max_length=60, blank=True, default="Birth to 21")
    show_in_overview = models.BooleanField(default=True, help_text="Show on the home page services list.")
    intro = RichTextField(features=["bold", "italic", "link"], blank=True)
    helps_with = models.TextField(blank=True, help_text="One item per line. Conditions and needs this service helps with.")
    what_we_offer = models.TextField(blank=True, help_text="One item per line.")
    first_visit = models.TextField(blank=True, help_text="What to expect at the first visit.")
    photo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+",
        help_text="One photo of this therapy, shown beside 'Your first visit'. It's cropped square around the image's "
        "focal point, so set the focal point on the image if faces get cut off. A real photo of your team at work is best.",
    )
    body = StreamField(BodyStreamBlock(), blank=True)

    content_panels = Page.content_panels + HeroMixin.hero_panels + [
        MultiFieldPanel(
            [FieldRowPanel([FieldPanel("short_name"), FieldPanel("icon"), FieldPanel("age_range")]), FieldPanel("summary"), FieldPanel("show_in_overview")],
            "Card",
        ),
        FieldPanel("intro"),
        FieldPanel("photo"),
        FieldPanel("helps_with"),
        FieldPanel("what_we_offer"),
        FieldPanel("first_visit"),
        FieldPanel("body"),
    ]
    parent_page_types = ["pages.ServiceIndexPage"]
    search_fields = Page.search_fields + [index.SearchField("summary"), index.SearchField("helps_with"), index.SearchField("body")]

    def siblings(self):
        return ServicePage.objects.sibling_of(self, inclusive=False).live().public()


DISCIPLINE_CHOICES = [
    ("audiology", "Audiology"),
    ("ot", "Occupational Therapy"),
    ("pt", "Physical Therapy"),
    ("slp", "Speech-Language Pathology"),
    ("office", "Front Office & Leadership"),
]

# Accent color for each discipline's cards, badges and filter buttons (names match COLOR_CHOICES / site.css).
DISCIPLINE_COLORS = {"audiology": "sky", "ot": "coral", "pt": "leaf", "slp": "grape", "office": "sun"}


class TeamMember(index.Indexed, models.Model):
    """A provider or staff member. Edited under "Providers" in the admin menu (see wagtail_hooks.py)."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, help_text="Used in the profile address. Filled in from the name if left blank.")
    credentials = models.CharField(max_length=80, blank=True, help_text="e.g. 'M.S., CCC-SLP'")
    title = models.CharField(max_length=100, blank=True, help_text="e.g. 'Clinical Coordinator'")
    discipline = models.CharField(max_length=20, choices=DISCIPLINE_CHOICES)
    photo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+",
        help_text="Cropped square around the image's focal point. A head-and-shoulders photo works best.",
    )
    bio = models.TextField(blank=True, help_text="One or two sentences for the team card.")
    intro = models.CharField(max_length=200, blank=True, help_text="Opening line on the profile, e.g. 'Meet Kimberly!'")
    licensure = models.TextField(blank=True, help_text="Licenses and certifications, one per line.")
    education = models.TextField(blank=True, help_text="Degrees, one per line.")
    experience = RichTextField(blank=True, features=["bold", "italic", "link", "ul"], help_text="Clinical experience and interests.")
    favorite_thing = models.CharField(max_length=140, blank=True, help_text="A fun line families and future teammates will remember.")
    is_clinician = models.BooleanField(default=True, help_text="Untick for front office staff. Only clinicians appear in the home page team row.")
    sort_order = models.IntegerField(default=0)

    panels = [
        FieldPanel("name"),
        FieldRowPanel([FieldPanel("credentials"), FieldPanel("title")]),
        FieldRowPanel([FieldPanel("discipline"), FieldPanel("is_clinician"), FieldPanel("sort_order")]),
        FieldPanel("slug"),
        FieldPanel("photo"),
        FieldPanel("bio"),
        MultiFieldPanel(
            [FieldPanel("intro"), FieldPanel("licensure"), FieldPanel("education"), FieldPanel("experience")],
            "Profile page",
        ),
        FieldPanel("favorite_thing"),
    ]
    search_fields = [index.SearchField("name"), index.SearchField("bio")]

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name = "provider"

    def __str__(self):
        return f"{self.name}, {self.credentials}" if self.credentials else self.name

    def save(self, *args, **kwargs):
        # Fill in a unique slug from the name (without "Dr.") when none was given.
        if not self.slug:
            base = slugify(self.name.replace("Dr.", "")) or "provider"
            slug, n = base, 2
            while TeamMember.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug, n = f"{base}-{n}", n + 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def url(self):
        """Profile address under the Our Providers page, or "" if that page isn't live."""
        team_page = TeamPage.objects.live().first()
        return f"{team_page.url}{self.slug}/" if team_page else ""

    @property
    def initials(self):
        parts = [p for p in self.name.replace("Dr.", "").split() if p[:1].isalpha()]
        return "".join(p[0] for p in parts[:2]).upper()

    @property
    def color(self):
        return DISCIPLINE_COLORS.get(self.discipline, "sun")


class TeamPage(RoutablePageMixin, HeroMixin, Page):
    """Our Providers. Lists every TeamMember by discipline and serves their profiles.

    Providers aren't pages, so their profile addresses (/our-providers/<slug>/)
    are routes on this page rather than child pages.
    """

    group_photo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+",
        help_text="A photo of the whole team, shown above the providers. Any shape works: the whole photo is shown, "
        "never cropped. Wider than tall, at least 1600 pixels across, looks best. Fill in the image's Description "
        "for screen readers. Until there is one, an illustration is shown.",
    )
    body = StreamField(BodyStreamBlock(), blank=True)

    content_panels = Page.content_panels + HeroMixin.hero_panels + [
        HelpPanel(
            content="<p><strong>Looking for the providers?</strong> Add, edit, reorder or remove them under "
                    "<a href=\"/admin/snippets/pages/teammember/\">Providers</a> in the left menu. "
                    "This page lists them automatically.</p>",
            heading="Providers",
        ),
        FieldPanel("group_photo"),
        FieldPanel("body"),
    ]
    max_count = 1

    @path("")
    def index(self, request):
        return self.render(request)

    @path("<slug:slug>/")
    def profile(self, request, slug):
        """One provider's profile, with up to four teammates from the same discipline."""
        member = TeamMember.objects.filter(slug=slug).first()
        if not member:
            raise Http404
        context = self.get_context(request)
        context["member"] = member
        context["teammates"] = TeamMember.objects.filter(discipline=member.discipline).exclude(pk=member.pk)[:4]
        return TemplateResponse(request, "pages/team_member.html", context)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        members = list(TeamMember.objects.all())
        groups = []
        for key, label in DISCIPLINE_CHOICES:
            group = [m for m in members if m.discipline == key]
            if group:
                groups.append({"key": key, "label": label, "color": DISCIPLINE_COLORS[key], "members": group})
        context["groups"] = groups
        return context


class CareersPage(HeroMixin, Page):
    """The Careers page. Lists its open, published JobPage children."""

    body = StreamField(BodyStreamBlock(), blank=True)
    no_openings_text = models.CharField(
        max_length=255, blank=True,
        default="No openings posted right now, but we always want to hear from great therapists.",
    )
    general_apply_email = models.EmailField(blank=True)

    content_panels = Page.content_panels + HeroMixin.hero_panels + [
        FieldPanel("body"), FieldPanel("no_openings_text"), FieldPanel("general_apply_email"),
    ]
    subpage_types = ["pages.JobPage"]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["jobs"] = JobPage.objects.child_of(self).live().public().filter(is_open=True)
        return context


class JobPage(HeroMixin, Page):
    """One job posting under Careers. Untick is_open to hide it without deleting it."""

    discipline = models.CharField(max_length=20, choices=DISCIPLINE_CHOICES)
    employment_type = models.CharField(max_length=40, default="Full-time")
    location = models.CharField(max_length=80, default="Acworth, GA")
    summary = models.TextField()
    body = StreamField(BodyStreamBlock(), blank=True)
    apply_email = models.EmailField(blank=True)
    apply_url = models.URLField(blank=True)
    is_open = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldRowPanel([FieldPanel("discipline"), FieldPanel("employment_type"), FieldPanel("location")]),
        FieldPanel("summary"),
        FieldPanel("body"),
        FieldRowPanel([FieldPanel("apply_email"), FieldPanel("apply_url")]),
        FieldPanel("is_open"),
    ]
    parent_page_types = ["pages.CareersPage"]

    @property
    def color(self):
        return DISCIPLINE_COLORS.get(self.discipline, "sun")


class ContactFormField(AbstractFormField):
    """A field on the contact form, edited inline on the Contact page."""

    page = ParentalKey("ContactPage", on_delete=models.CASCADE, related_name="form_fields")


LUXSCI_FORM_NAME = "secureform"  # LuxSci matches this name, case sensitive


class ContactPage(HeroMixin, AbstractEmailForm):
    """Contact Us: a form, map and contact details.

    With a LuxSci code, the visitor's browser posts the form straight to LuxSci
    (HIPAA-secure), so messages never reach this server, and LuxSci sends them
    back to ?sent=1 for the thank-you text. Without one, it's an ordinary Wagtail
    form that saves submissions in the admin and emails them.
    """

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    luxsci_form_id = models.CharField(
        "LuxSci Secure Form code", max_length=60, blank=True,
        help_text="e.g. 18249-26830-Zg4g. When filled in, messages go to LuxSci (HIPAA-secure, with spam "
        "protection) instead of being saved in this admin. Leave blank to save messages here.",
    )

    content_panels = AbstractEmailForm.content_panels + HeroMixin.hero_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldPanel("luxsci_form_id"),
                HelpPanel(
                    "In LuxSci, set the page shown after sending to this page's address followed by ?sent=1 "
                    "(for example https://beyondlimitstherapy.org/contact/?sent=1) so families see the thank-you text above."
                ),
            ],
            "Secure form (LuxSci)",
        ),
        MultiFieldPanel(
            [FieldRowPanel([FieldPanel("from_address"), FieldPanel("to_address")]), FieldPanel("subject")],
            "Email (only used when there's no LuxSci code)",
        ),
    ]

    @property
    def luxsci_action_url(self):
        """Where the form posts when LuxSci is on."""
        return f"https://secureform.luxsci.com/perl/post/{self.luxsci_form_id}"

    @property
    def luxsci_script_url(self):
        """LuxSci's script, which adds its spam protection to the form named LUXSCI_FORM_NAME."""
        return f"https://secureform.luxsci.com/intranet/php/secureform.php?v=1&c={self.luxsci_form_id}&f={LUXSCI_FORM_NAME}"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["sent"] = request.GET.get("sent") == "1"
        return context

    def serve(self, request, *args, **kwargs):
        # With LuxSci on, messages must never be posted (and saved or logged) here.
        if request.method == "POST" and self.luxsci_form_id:
            return HttpResponseNotAllowed(["GET"])
        return super().serve(request, *args, **kwargs)
