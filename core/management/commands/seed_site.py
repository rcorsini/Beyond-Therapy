"""Build the starter page tree and content for the Beyond Limits site.

Content comes from beyondlimitstherapy.org and the developer's build
(services, providers, insurance, veterans, resources). Provider profiles in
core/fixtures/provider_profiles.json are lightly summarized from the developer's
build and should be checked by each provider. Careers copy is a draft for the
clinic to review.

    python manage.py seed_site          # only if the site has not been seeded
    python manage.py seed_site --reset  # delete the existing pages and rebuild
"""

import json
import uuid
from pathlib import Path

from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.html import escape

from wagtail.images import get_image_model
from wagtail.images.rect import Rect
from wagtail.models import Page, Site

from core.models import ClinicSettings
from home.models import HomePage
from pages.models import (
    CareersPage,
    ContactFormField,
    ContactPage,
    JobPage,
    ServiceIndexPage,
    ServicePage,
    StandardPage,
    TeamMember,
    TeamPage,
)


def block(type_, value):
    return {"type": type_, "value": value, "id": str(uuid.uuid4())}


def stream(*blocks):
    """Raw StreamField JSON, so page links can be given as ids."""
    return json.dumps(list(blocks))


def link(label="", page=None, url="", anchor=""):
    return {"label": label, "page": page.pk if page else None, "external_url": url, "anchor": anchor}


def heading(heading_, eyebrow="", intro=""):
    return {"eyebrow": eyebrow, "heading": heading_, "intro": intro}


# Starter photos (stock until the clinic's own arrive) live in core/seed_images.
# Any file that isn't there yet is skipped, and the page shows its illustration.
SEED_IMAGES = Path(__file__).resolve().parents[2] / "seed_images"


def seed_image(filename, title, description=""):
    path = SEED_IMAGES / filename
    if not path.exists():
        return None
    Image = get_image_model()
    existing = Image.objects.filter(title=title).first()
    if existing:
        return existing
    with path.open("rb") as f:
        return Image.objects.create(title=title, description=description, file=ImageFile(f, name=filename))


def image_id(filename, title):
    img = seed_image(filename, title)
    return img.pk if img else None


def seed_headshot(member):
    """Loads core/seed_images/providers/<slug>.jpg as the provider's photo, if it exists."""
    img = seed_image(f"providers/{member.slug}.jpg", f"{member.name} headshot (starter photo)")
    if not img:
        return
    if not img.has_focal_point() and img.height > img.width:
        # Headshots are cropped square; aim at the upper part of a tall photo so the face stays in frame.
        img.set_focal_point(Rect.from_point(img.width // 2, img.height // 3, img.width // 2, img.height // 3))
        img.save()
    member.photo = img
    member.save(update_fields=["photo"])


PROVIDERS = [
    # name, credentials, title, discipline, is_clinician
    ("Dr. Kimberly Oviedo", "Au.D.", "Executive Director", "audiology", True),
    ("Dr. Karen Mobley", "Au.D.", "", "audiology", True),
    ("Dr. Ashley Moore", "Au.D.", "", "audiology", True),
    ("Amy Austin", "M.S., OTR/L", "", "ot", True),
    ("Debbie Jerome", "OTR/L", "Clinical Coordinator", "ot", True),
    ("Andrea Nguyen", "PT", "", "pt", True),
    ("Mary-Katherine Burton", "PT, DPT", "", "pt", True),
    ("Autumn Pacheco", "PT, DPT", "", "pt", True),
    ("Bailey Burch", "PT, DPT", "", "pt", True),
    ("Tyra", "PT, DPT", "", "pt", True),
    ("Shayla Singleton", "M.Ed., CCC-SLP", "", "slp", True),
    ("Shari Cottle", "M.Ed., CCC-SLP", "PRN", "slp", True),
    ("Carl Deal", "M.S., CCC-SLP", "", "slp", True),
    ("Tammy Southers", "SLP", "PRN", "slp", True),
    ("Emily Whitworth", "M.Ed., CCC-SLP", "PRN", "slp", True),
    ("Kara Klayman", "M.S., CCC-SLP", "PRN", "slp", True),
    ("Hunter Bruce", "M.Ed., CCC-SLP", "", "slp", True),
    ("Caroline Hamby", "M.Ed., CCC-SLP", "", "slp", True),
    ("Allison Williams", "M.S., CCC-SLP", "", "slp", True),
    ("Michelle Tippens", "M.S., CF-SLP", "", "slp", True),
    ("Addie Smith", "CCC-SLP", "", "slp", True),
    ("Krystal Von Ruden", "CCC-SLP", "", "slp", True),
    ("Emily", "CF-SLP", "", "slp", True),
    ("Madison Chalker", "", "Billing Specialist & New Patient Advocate", "office", False),
    ("Lailah Senegal", "", "Scheduling Coordinator", "office", False),
    ("Mandy Bridges", "", "Scheduling Coordinator", "office", False),
]

SERVICES = [
    {
        "title": "Audiology",
        "slug": "pediatric-audiology",
        "short_name": "Audiology",
        "icon": "ear",
        "hero_color": "sky",
        "summary": "Hearing screenings and full diagnostic testing for newborns, kids and young adults, so nothing stands in the way of learning to listen and talk.",
        "hero_intro": "Early answers about hearing make a big difference. Our audiologists test babies from their first days through age 21.",
        "intro": "<p>About five out of every 1,000 babies are born with some degree of hearing loss. Finding it early gives your child the best start with speech, language and learning. Our doctors of audiology use child-friendly testing so even the youngest patients can show us what they hear.</p>",
        "helps_with": "Newborns who need a follow-up hearing screen\nBabies and kids with suspected hearing loss\nSpeech or language delays that might be hearing-related\nFrequent ear infections or fluid behind the ear\nKids who need custom ear molds\nChildren starting speech therapy who need a hearing check",
        "what_we_offer": "Diagnostic ABR testing\nNewborn hearing screening (AABR and OAE)\nComprehensive hearing evaluations (VRA, play audiometry, standard audiometry)\nMiddle ear and Eustachian tube testing\nCustom ear molds\nHearing checks for speech-language patients",
        "first_visit": "Plan on about an hour. We'll talk with you about your child's history, then use play-based listening games or a quiet sleep test for babies. You'll leave with results explained in plain language and clear next steps.",
    },
    {
        "title": "Occupational Therapy",
        "slug": "pediatric-occupational-therapy",
        "short_name": "OT",
        "icon": "hand",
        "hero_color": "coral",
        "summary": "Building the everyday skills kids need for home, school and play, from feeding and dressing to handwriting and handling big feelings.",
        "hero_intro": "Occupational therapy helps your child do the things they want and need to do every day, with more confidence and independence.",
        "intro": "<p>Our occupational therapists work on fine motor, sensory-motor and visual-motor skills through play. Sessions happen in our sensory gyms and treatment rooms, and you'll get a home program so progress keeps going between visits.</p>",
        "helps_with": "Autism spectrum disorder\nADD and ADHD\nSensory processing differences\nDevelopmental delays and disabilities\nDown syndrome and other genetic conditions\nCerebral palsy\nOther neurological diagnoses\nFeeding challenges and picky eating\nTraumatic brain injury",
        "what_we_offer": "Full OT evaluations\nPlay-based therapy in our sensory gyms\nFeeding therapy\nHandwriting and fine motor skills\nDressing, self-care and daily routines\nSensory regulation, balance and attention\nParent coaching and home programs",
        "first_visit": "Your child's therapist will spend time playing and observing, and you'll fill us in on what's hard at home and school. Together we'll set goals that matter to your family.",
    },
    {
        "title": "Physical Therapy",
        "slug": "pediatric-physical-therapy",
        "short_name": "PT",
        "icon": "run",
        "hero_color": "leaf",
        "summary": "Helping kids move, play and keep up, with therapy for strength, balance, coordination and walking.",
        "hero_intro": "From a baby's first roll to a teen getting back on the field, our physical therapists help kids move with strength and confidence.",
        "intro": "<p>Every child gets an individualized plan and a home program. Our two large therapy gyms are built for movement, with parent viewing windows so you can watch your child work.</p>",
        "helps_with": "Congenital muscular torticollis\nPositional plagiocephaly (flat head)\nCerebral palsy\nSpina bifida\nToe walking\nPrematurity and motor delays\nSports injuries\nTraumatic brain injury",
        "what_we_offer": "Manual therapy\nTherapeutic exercise and strengthening\nGait training\nKinesiotaping\nMotor planning and coordination\nHelp with daily care and positioning\nRecommendations for assistive devices, orthotics and prosthetics",
        "first_visit": "We'll look at how your child moves, plays and gets around, and talk with you about your goals. Wear comfy clothes and bring any braces or equipment your child uses.",
    },
    {
        "title": "Speech-Language Therapy",
        "slug": "speech-language-therapy",
        "short_name": "Speech",
        "icon": "speech",
        "hero_color": "grape",
        "summary": "Helping kids find their words and their voice, including talking, understanding, social communication and AAC devices.",
        "hero_intro": "Communication is how kids connect. Our speech-language pathologists help every child be understood, whether that's with words, signs or a device.",
        "intro": "<p>Our speech-language pathologists assess, diagnose and treat speech and language delays and disorders. We support social communication and augmentative and alternative communication (AAC), and we work closely with our audiologists when hearing is part of the picture.</p>",
        "helps_with": "Autism spectrum disorder\nLate talkers and language delays\nApraxia of speech\nStuttering and fluency\nVoice disorders\nHearing impairment\nOral motor weakness\nFeeding challenges and picky eating\nDown syndrome and other genetic conditions",
        "what_we_offer": "Articulation and phonology\nReceptive and expressive language\nSocial communication\nAAC evaluation and support\nFluency and voice therapy\nCognitive-communication\nFeeding therapy with our OT team",
        "first_visit": "Your child's evaluation will feel like play. We'll listen, talk, read and play together, then share what we found and how therapy can help.",
    },
]


class Command(BaseCommand):
    help = "Create the starter pages, settings and team for the Beyond Limits site."

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true", help="Delete existing pages first.")

    @transaction.atomic
    def handle(self, *args, **options):
        root = Page.get_first_root_node()
        if HomePage.objects.exists():
            if not options["reset"]:
                self.stdout.write("Site already seeded. Use --reset to rebuild.")
                return
        # Remove everything under the tree root (Wagtail's welcome page or an older seed).
        for child in root.get_children():
            child.delete()
        TeamMember.objects.all().delete()
        # Reload starter photos so swapped files in core/seed_images take effect.
        get_image_model().objects.filter(title__endswith="(starter photo)").delete()
        root.refresh_from_db()

        home = root.add_child(instance=HomePage(title="Home", slug="home"))
        Site.objects.all().delete()
        site = Site.objects.create(
            hostname="localhost", port=80, root_page=home, is_default_site=True,
            site_name="Beyond Limits Pediatric Therapy Center",
        )

        def add(parent, page):
            parent.add_child(instance=page)
            page.save_revision().publish()
            return page

        about = add(home, StandardPage(
            title="About Us", slug="about-us", show_in_menus=True, hero_color="sky",
            hero_intro="Founded by parents of children with special needs, Beyond Limits brings exceptional pediatric therapy together in one place.",
        ))
        services = add(home, ServiceIndexPage(
            title="Services", slug="services", show_in_menus=True, hero_color="indigo",
            hero_intro="Audiology, occupational, physical and speech-language therapy for ages birth to 21, all under one roof in Acworth.",
        ))
        service_pages = {}
        for data in SERVICES:
            photo = seed_image(f"service-{data['slug']}.jpg", f"{data['title']} (starter photo)")
            service_pages[data["short_name"]] = add(services, ServicePage(photo=photo, **data))
        team = add(home, TeamPage(
            title="Our Providers", slug="our-providers", show_in_menus=True, hero_color="leaf",
            # The clinic's real team photo when it arrives; until then Russell's stand-in, here only.
            group_photo=seed_image("team-group.jpg", "Team photo (starter photo)")
            or seed_image("providers-standin.jpg", "Providers team photo stand-in (starter photo)",
                          "A team of nine therapists smiling together in a pediatric therapy gym"),
            hero_intro="Board-certified therapists with extra pediatric training, and a front office that will know your child by name.",
        ))
        get_started = add(home, StandardPage(
            title="Get Started", slug="get-started", show_in_menus=True, hero_color="sun",
            hero_intro="New to Beyond Limits? Here's exactly what happens, from your first call to your child's first session.",
        ))
        resources = add(home, StandardPage(
            title="Resources", slug="resources", show_in_menus=True, hero_color="teal",
            hero_intro="Organizations, reading and family support we trust, gathered in one place.",
        ))
        contact = add(home, ContactPage(
            title="Contact Us", slug="contact", show_in_menus=True, hero_color="coral",
            hero_intro="Call or text us, stop by, or send a note. We'll get back to you within one business day.",
            intro="<p>Questions about therapy, insurance or scheduling? Send us a message and our new patient advocate will reach out.</p>",
            thank_you_text="<p>Thanks for reaching out! Someone from our front office will contact you within one business day.</p>",
            to_address="info@blptc.org", from_address="website@blptc.org", subject="Website message",
            luxsci_form_id="18249-26830-Zg4g",
        ))
        careers = add(home, CareersPage(
            title="Careers", slug="careers", show_in_menus=False, hero_color="indigo",
            hero_intro="Do the work you trained for, with a team that has your back. We're always looking for therapists who love working with kids.",
            general_apply_email="info@blptc.org",
        ))
        veterans = add(home, StandardPage(
            title="Veterans Hearing Evaluations", slug="veterans", show_in_menus=False, hero_color="navy",
            hero_intro="Our audiologists are honored to provide hearing evaluations for veterans and active-duty service members through VES.",
        ))
        privacy = add(home, StandardPage(
            title="HIPAA Privacy Policy", slug="hipaa-privacy-policy", show_in_menus=False, hero_color="sky",
            hero_intro="How we protect and use your family's health information.",
        ))

        first_visit = add(home, StandardPage(
            title="Your First Visit in Photos", slug="first-visit", show_in_menus=False, hero_color="sky",
            hero_intro="A step-by-step photo story to look at with your child before the first appointment, so nothing is a surprise.",
        ))
        insurance = add(home, StandardPage(
            title="Insurance and Your First Visit", slug="insurance", show_in_menus=False, hero_color="teal",
            hero_intro="What we'll check before your child's first visit, what to bring, and how long it takes to get started.",
        ))

        for i, (sort, label, ftype, required, choices) in enumerate([
            (1, "Your name", "singleline", True, ""),
            (2, "Phone", "singleline", True, ""),
            (3, "Email", "email", True, ""),
            (4, "I'm interested in", "dropdown", False, "Not sure yet\nAudiology\nOccupational Therapy\nPhysical Therapy\nSpeech-Language Therapy\nVeterans hearing evaluation\nCareers"),
            (5, "How can we help?", "multiline", True, ""),
        ]):
            ContactFormField.objects.create(page=contact, sort_order=sort, label=label, field_type=ftype, required=required, choices=choices)

        profiles = json.loads((Path(__file__).resolve().parents[2] / "fixtures" / "provider_profiles.json").read_text())
        for i, (name, creds, title, disc, clinician) in enumerate(PROVIDERS):
            p = profiles.get(name, {})
            experience = "".join(f"<p>{escape(para.strip())}</p>" for para in p.get("experience", "").split("\n\n") if para.strip())
            member = TeamMember.objects.create(
                name=name, credentials=creds, title=title, discipline=disc, is_clinician=clinician, sort_order=i,
                intro=p.get("intro", ""), licensure="\n".join(p.get("licensure", [])),
                education="\n".join(p.get("education", [])), experience=experience,
            )
            seed_headshot(member)

        settings = ClinicSettings.load()
        settings.clinic_name = "Beyond Limits Pediatric Therapy Center"
        settings.short_name = "Beyond Limits"
        settings.tagline = "Comprehensive pediatric therapy for ages birth to 21, all in one place."
        settings.phone = "770-917-5737"
        settings.fax = "770-917-5740"
        settings.email = "info@blptc.org"
        settings.address_line_1 = "4900 Ivey Road, Ste. 1720"
        settings.address_line_2 = "Acworth, GA 30101"
        settings.hours = "Mon to Fri, 8:00 AM to 6:00 PM"
        settings.map_embed_url = "https://maps.google.com/maps?q=4900%20Ivey%20Road%20Ste%201720%20Acworth%20GA%2030101&output=embed"
        settings.directions_url = "https://www.google.com/maps/dir/?api=1&destination=4900+Ivey+Road+Ste+1720+Acworth+GA+30101"
        settings.start_page = get_started
        settings.veterans_page = veterans
        settings.veterans_label = "Veterans hearing exams"
        settings.careers_page = careers
        settings.privacy_page = privacy
        settings.insurance_page = insurance
        settings.first_visit_page = first_visit
        settings.secure_contact_url = "https://secureform.luxsci.com/forms/18016/11369/XuRN/form.html"
        settings.save()

        # ---------------- Home ----------------
        home.slides = stream(
            block("slide", {
                "image": image_id("slide-1.jpg", "Home slide 1 (starter photo)"),
                "background": "indigo", "illustration": "hero", "box_color": "indigo",
                "eyebrow": "Beyond Limits Pediatric Therapy Center",
                "title": "Helping kids thrive.",
                "text": "Founded by parents in 2014. More than 750 kids every week, from birth to 21.",
                "button": link("New family admission forms", get_started, anchor="forms"),
                "note": "Questions first? Call or text 770-917-5737.",
            }),
            block("slide", {
                "image": image_id("slide-2.jpg", "Home slide 2 (starter photo)"),
                "background": "leaf", "illustration": "team", "box_color": "teal",
                "eyebrow": "Care that fits your child",
                "title": "Autism, sensory and developmental care.",
                "text": "Speech, OT, PT and audiology specialists who plan your child's care together.",
                "button": link("See what to look for", services, anchor="does-this-sound-like-your-child"),
                "note": "",
            }),
            block("slide", {
                "image": image_id("slide-3.jpg", "Home slide 3 (starter photo)"),
                "background": "sky", "illustration": "gym", "box_color": "sky",
                "eyebrow": "9,000 sq. ft. made for play",
                "title": "A clinic built for kids.",
                "text": "Two therapy gyms, two sensory gyms, feeding rooms and parent viewing windows.",
                "button": link("Take the photo tour", first_visit),
                "note": "",
            }),
            block("slide", {
                # The clinic's real team photo only: a stock "team" would pass strangers off as staff.
                "image": image_id("team-group.jpg", "Team photo (starter photo)"),
                "background": "grape", "illustration": "garden", "box_color": "grape",
                "eyebrow": "Now hiring therapists",
                "title": "Love what you do here.",
                "text": "Join a team of pediatric specialists who mentor each other and celebrate every win.",
                "button": link("See careers", careers),
                "note": "",
            }),
        )
        home.body = stream(
            block("quick_links", {"links": [
                {"title": "New family admission forms", "text": "Complete before scheduling with us", "link": link("", get_started)},
                {"title": "Our providers", "text": "Meet the people behind the progress", "link": link("", team)},
                {"title": "Join our team", "text": "Therapists, see why people love working here", "link": link("", careers)},
            ]}),
            block("split", {
                "eyebrow": "Care that grows with your child",
                "heading": "Helping kids thrive, from birth through young adulthood",
                "text": "<p>Beyond Limits Pediatric Therapy Center in Acworth, GA provides comprehensive screening, diagnostics and therapy for children and young adults from birth to age 21, all in one place.</p>"
                        "<h3>What families can expect</h3><ul>"
                        "<li>Licensed, board-certified therapists with advanced pediatric training</li>"
                        "<li>A care plan built around your child's needs and your family's goals</li>"
                        "<li>A calm, kid-friendly clinic with sensory gyms and parent viewing windows</li>"
                        "<li>Help with insurance and paperwork before your first visit</li></ul>",
                "image": None, "illustration": "blocks", "image_side": "left",
                "button": link("Get started", get_started),
            }),
            block("services_overview", {"heading": heading("Our therapy services", "Growing skills, building confidence")}),
            block("stats", {"stats": [
                {"number": "750+", "label": "kids helped every week"},
                {"number": "4", "label": "therapies under one roof"},
                {"number": "9,000", "label": "sq. ft. clinic built for kids"},
                {"number": "2014", "label": "founded by parents"},
            ]}),
            block("split", {
                "eyebrow": "Our philosophy",
                "heading": "Taking your child beyond their limits",
                "text": "<p>Progress happens when the child, the family and the care team work together. We set goals with you, share what we're working on, and give you simple ways to keep the momentum going at home.</p>"
                        "<p>Our clinic has two large therapy gyms, two sensory gyms, two feeding therapy rooms, private treatment rooms and a work bar where parents can get things done while they wait.</p>",
                "image": None, "illustration": "gym", "image_side": "right",
                "button": link("About us", about),
            }),
            block("testimonial", {
                "quote": "Thanks to Beyond Limits and their amazing therapists I know that she will grow up without limits.",
                "name": "Melisa Chun", "role": "Grace's mom",
            }),
            block("cards", {"heading": heading("The Super Six", "Our core values", "Six promises every member of our team makes to every family."), "cards": [
                {"icon": "heart", "color": "coral", "title": "Passion", "text": "We love what we do, and kids can tell.", "link": link()},
                {"icon": "calendar", "color": "sky", "title": "Disciplined", "text": "Consistent, evidence-based care, session after session.", "link": link()},
                {"icon": "chat", "color": "teal", "title": "Transparent", "text": "Honest updates, clear goals and no surprises.", "link": link()},
                {"icon": "check", "color": "sun", "title": "Accountable", "text": "We own our work and your child's progress. It's central to our success.", "link": link()},
                {"icon": "users", "color": "grape", "title": "Teamwork", "text": "Therapists, families and doctors working as one.", "link": link()},
                {"icon": "star", "color": "leaf", "title": "Excellence", "text": "Always learning so every child gets our best.", "link": link()},
            ]}),
            block("team_teaser", {
                "heading": heading("Meet the people behind the progress", "Our team"),
                "count": 8, "button": link("Meet all our providers", team),
            }),
            block("careers_band", {
                "eyebrow": "Work with us",
                "heading": "Love what you do. Grow while you do it.",
                "text": "We're a close team of audiologists, OTs, PTs and SLPs who mentor each other and celebrate every win, big or small.",
                "points": [
                    "Mentorship for new grads and clinical fellows",
                    "Work alongside every pediatric discipline",
                    "Sensory gyms and space built for great therapy",
                ],
                "button": link("See open roles", careers), "image": None,
            }),
            block("steps", {"heading": heading("Here for your family", "Your next steps"), "steps": [
                {"title": "New patient admission forms", "text": "Fill these out before your first visit.", "link": link("Start here", get_started)},
                {"title": "Resources", "text": "Trusted organizations and family support.", "link": link("View resources", resources)},
                {"title": "Our providers", "text": "Get to know your child's care team.", "link": link("View our providers", team)},
                {"title": "Schedule a tour", "text": "Come see the gyms and meet the team.", "link": link("See the clinic", contact)},
            ]}),
        )
        home.save_revision().publish()

        # ---------------- About ----------------
        about.body = stream(
            block("split", {
                "eyebrow": "Our story", "heading": "Started by parents, for families like yours",
                "text": "<p>Beyond Limits opened in March 2014, founded by parents of children with special needs. Their vision was simple: bring exceptional pediatric therapy together in one convenient place, so families don't have to drive all over town for care.</p>"
                        "<p>Today we provide audiology, occupational therapy, physical therapy and speech-language therapy for more than 750 children every week.</p>",
                "image": None, "illustration": "garden", "image_side": "right", "button": link("Meet our providers", team),
            }),
            block("stats", {"stats": [
                {"number": "750+", "label": "kids every week"},
                {"number": "9,000", "label": "sq. ft. ADA-accessible clinic"},
                {"number": "4", "label": "pediatric therapies"},
                {"number": "0-21", "label": "ages we serve"},
            ]}),
            block("cards", {"heading": heading("Inside our clinic", "Built for kids"), "cards": [
                {"icon": "run", "color": "leaf", "title": "Two therapy gyms", "text": "Big, bright spaces with parent viewing windows.", "link": link()},
                {"icon": "sparkle", "color": "grape", "title": "Two sensory gyms", "text": "Swings, crash pads and calm corners for regulation.", "link": link()},
                {"icon": "heart", "color": "coral", "title": "Feeding therapy rooms", "text": "Two dedicated rooms for feeding and mealtime skills.", "link": link()},
                {"icon": "home", "color": "sky", "title": "Comfortable waiting areas", "text": "Two waiting rooms, free Wi-Fi and a work bar for parents.", "link": link()},
            ]}),
            block("heading", heading("Taking your child beyond their limits", "Our philosophy")),
            block("paragraph", "<p>Our therapists are board-certified professionals with additional pediatric training. They partner with you and your child's doctors to set goals that matter, and they keep you in the loop every step of the way. Our commitment is to help each child reach, and go beyond, their own goals.</p>"),
            block("cta", {"color": "sun", "title": "Want to see the clinic?", "text": "We'd love to show you around. Call or text to schedule a tour.",
                          "button": link("Contact us", contact), "secondary_button": link("Get started", get_started)}),
        )
        about.save_revision().publish()

        # ---------------- Services index ----------------
        services.body = stream(
            block("signs", {
                "heading": heading("Does this sound like your child?", "Not sure where to start?",
                                   "You know your child best. If a few of these sound familiar, that therapy is a good place to begin. "
                                   "Many kids benefit from more than one, and we'll help you sort it out."),
                "anchor": "does-this-sound-like-your-child",
                "cards": [
                    {"type": "item", "id": str(uuid.uuid4()), "value": {
                        "title": "Everyday tasks and senses", "icon": "hand", "color": "coral",
                        "signs": "Struggles with buttons, zippers, scissors or a pencil\nIs upset by noise, clothing tags, haircuts or messy hands\nHas a hard time calming down after big feelings\nAvoids or seeks out lots of swinging, spinning or crashing",
                        "link": link("Occupational therapy", service_pages["OT"])}},
                    {"type": "item", "id": str(uuid.uuid4()), "value": {
                        "title": "Talking and understanding", "icon": "speech", "color": "grape",
                        "signs": "Says fewer words than other kids the same age\nIs hard for others to understand\nGets frustrated trying to tell you what they want\nStutters, or has a hoarse voice that doesn't go away",
                        "link": link("Speech-language therapy", service_pages["Speech"])}},
                    {"type": "item", "id": str(uuid.uuid4()), "value": {
                        "title": "Moving and playing", "icon": "run", "color": "leaf",
                        "signs": "Sat up, crawled or walked later than expected\nTrips or falls more than other kids\nWalks on tiptoes much of the time\nTires quickly, or finds stairs, jumping or catching hard",
                        "link": link("Physical therapy", service_pages["PT"])}},
                    {"type": "item", "id": str(uuid.uuid4()), "value": {
                        "title": "Eating and mealtimes", "icon": "heart", "color": "sun",
                        "signs": "Eats only a handful of foods\nGags, coughs or chokes often while eating\nHas trouble moving from purees to solid foods\nMealtimes are a daily struggle",
                        "link": link("Feeding therapy (OT and speech)", service_pages["OT"])}},
                    {"type": "item", "id": str(uuid.uuid4()), "value": {
                        "title": "Hearing and listening", "icon": "ear", "color": "sky",
                        "signs": "Doesn't respond to their name or to sounds\nTurns the TV up loud or often says \"what?\"\nNeeds a recheck after a newborn hearing screening\nHas a lot of ear infections",
                        "link": link("Audiology", service_pages["Audiology"])}},
                    {"type": "item", "id": str(uuid.uuid4()), "value": {
                        "title": "Autism, or just not sure", "icon": "puzzle", "color": "teal",
                        "signs": "Your child was recently diagnosed with autism\nPlays alone, or the same way over and over\nRarely points, waves or looks at you to share something\nSomething feels different, and you'd like a second opinion",
                        "link": link("Call or text us to talk it through", contact)}},
                ],
            }),
            block("cta", {"color": "teal", "title": "Not sure where to start?",
                          "text": "Many kids benefit from more than one therapy. Call or text and we'll help you figure out the right first step.",
                          "button": link("Get started", get_started), "secondary_button": link("Contact us", contact)}),
        )
        services.save_revision().publish()

        # ---------------- Get started ----------------
        # Secure online forms the clinic already uses (LuxSci, linked from beyondlimitstherapy.org/admission-forms/).
        lux = "https://secureform.luxsci.com/forms/18016/"
        online = {
            "General Admissions Form": lux + "12134/J1HD/form.html",
            "General Admission with Upper Extremity Intake Form": lux + "23214/J9P3/form.html",
            "ST/OT Feeding Intake Form": lux + "24532/jCRG/form.html",
            "Audiology Admission|Newborn to 12 months": lux + "22903/xOy1/form.html",
            "Audiology Admission|13 months to school age": lux + "22904/R68Q/form.html",
            "Patient Update Form": lux + "18856/JHPn/form.html",
            "Telehealth Consent Form": lux + "15983/hFgB/form.html",
            "Payment Consent Form": lux + "18866/Q5Lr/form.html",
        }

        def form(title, note=""):
            url = online.get(f"{title}|{note}") or online.get(title, "")
            return {"title": title, "online_url": url, "document": None, "note": note}

        new_family_forms = [form("Payment Consent Form")]
        get_started.body = stream(
            block("form_finder", {
                "heading": heading("Find the right forms", "Step one", "Answer one or two quick questions and we'll show you exactly what to fill out."),
                "question": "What brings you here today?",
                "return_note": "<p><b>Online forms</b> go straight to our office through a secure, HIPAA-compliant connection. For a PDF, email it to info@blptc.org, fax it to 770-917-5740, or bring it to your first visit.</p>",
                "paths": [
                    {
                        "label": "My child is new to Beyond Limits", "description": "Starting therapy or a hearing test", "icon": "family",
                        "follow_up_question": "Which service is your child starting with?",
                        "options": [
                            {"label": "Speech-language therapy", "forms": [form("General Admissions Form")], "note": ""},
                            {"label": "Occupational therapy", "forms": [form("General Admissions Form")], "note": "<p>If the main concern is using an arm or hand, use the General Admission with Upper Extremity Intake Form instead.</p>"},
                            {"label": "Physical therapy", "forms": [form("General Admissions Form")], "note": ""},
                            {"label": "Feeding therapy", "forms": [form("General Admissions Form"), form("ST/OT Feeding Intake Form")], "note": ""},
                            {"label": "Hearing test, baby under 13 months", "forms": [form("Audiology Admission", "Newborn to 12 months")], "note": ""},
                            {"label": "Hearing test, 13 months to school age", "forms": [form("Audiology Admission", "13 months to school age")], "note": ""},
                            {"label": "Not sure yet", "forms": [], "note": "<p>No problem. Call or text 770-917-5737 and our new patient advocate will help you figure out where to start.</p>"},
                        ],
                        "forms": new_family_forms + [form("Telehealth Consent Form", "Only if your child will have telehealth sessions")],
                        "note": "", "button": link(),
                    },
                    {
                        "label": "My child already comes here", "description": "Updating info or adding a service", "icon": "heart",
                        "follow_up_question": "What do you need to do?",
                        "options": [
                            {"label": "Update our address, insurance or contact info", "forms": [form("Patient Update Form")], "note": ""},
                            {"label": "Start telehealth sessions", "forms": [form("Telehealth Consent Form")], "note": ""},
                            {"label": "Add another therapy", "forms": [], "note": "<p>Let your child's therapist or our front desk know. We'll check whether new paperwork is needed.</p>"},
                        ],
                        "forms": [], "note": "", "button": link(),
                    },
                    {
                        "label": "I need medical records", "description": "For you, a school or another provider", "icon": "clipboard",
                        "follow_up_question": "", "options": [],
                        "forms": [{"title": "Medical Records Request and Disclosure", "online_url": "", "document": None, "note": "Printable PDF. Upload it under Documents to enable the download."}],
                        "note": "", "button": link(),
                    },
                    {
                        "label": "I'm a veteran with a VES appointment", "description": "Hearing evaluations for VES", "icon": "flag",
                        "follow_up_question": "", "options": [], "forms": [],
                        "note": "<p>You don't need any of our patient forms. Bring your photo ID and your VES appointment details.</p>",
                        "button": link("Veterans hearing evaluations", veterans),
                    },
                    {
                        "label": "I'm a doctor or school referring a child", "description": "Sending a referral or prescription", "icon": "users",
                        "follow_up_question": "", "options": [], "forms": [],
                        "note": "<p>Fax the referral or prescription to 770-917-5740, or call 770-917-5737. We'll contact the family to get them scheduled.</p>",
                        "button": link("Contact our office", contact, anchor="visit-or-call"),
                    },
                ],
            }),
            block("steps", {"heading": heading("What happens next", "From first call to first session"), "steps": [
                {"title": "Call or text us", "text": "Share your insurance, your child's doctor and any evaluation from the last 6 months.", "link": link()},
                {"title": "We check your benefits", "text": "You'll know your costs and any authorization needs before the first visit.", "link": link()},
                {"title": "Evaluation", "text": "Your child's therapist meets you both and writes a plan of care.", "link": link()},
                {"title": "Therapy begins", "text": "Once your doctor signs the plan and insurance approves (usually about 2 weeks), we call to schedule.", "link": link()},
            ]}),
            block("checklist", {"title": "Insurance we're in network with", "color": "sky", "items": [
                "Amerigroup", "CareSource", "Peach State", "BlueCross", "Ambetter", "Tricare", "Wellcare (Audiology only)",
            ]}),
            block("callout", {"color": "sun", "icon": "shield", "title": "Plan not listed?",
                              "text": "<p>We can still help. Call us and we'll check your out-of-network benefits.</p>",
                              "button": link("Contact us", contact)}),
            block("faq", {"heading": "Common questions", "items": [
                {"question": "Do I need a referral?", "answer": "<p>Most insurance plans need a prescription from your child's doctor. Give us the doctor's name and we'll request it for you. If you already have one, send us a copy before scheduling.</p>"},
                {"question": "How long until my child's first appointment?", "answer": "<p>After the evaluation, it usually takes about two weeks to get the doctor's signature on the plan of care and any prior authorization from insurance. We'll call you as soon as it's approved.</p>"},
                {"question": "My child has an IEP. Do you need it?", "answer": "<p>Yes, please. We share it with your child's therapist and some insurers need it for authorization. Send us the updated IEP whenever the school renews it.</p>"},
                {"question": "Can I watch my child's session?", "answer": "<p>Our therapy gyms have parent viewing windows, and therapists check in with you at the end of each session.</p>"},
            ]}),
        )
        get_started.save_revision().publish()

        # ---------------- Insurance and first visit ----------------
        insurance.body = stream(
            block("checklist", {"title": "Insurance we're in network with", "color": "sky", "items": [
                "Amerigroup", "CareSource", "Peach State", "BlueCross", "Ambetter", "Tricare", "Wellcare (Audiology only)",
            ]}),
            block("paragraph", "<p>Every plan above is in network for audiology. Wellcare covers audiology only, not occupational, physical or speech therapy. "
                               "If your plan isn't listed, we're out of network with it, but we're happy to check your out-of-network benefits for you.</p>"),
            block("heading", heading("Before your first visit", "No surprises")),
            block("paragraph", "<p>Once you call to set up an appointment, we use your insurance information to check your benefits. Before your child's first visit, you'll know:</p>"
                               "<ul><li>Your deductible, copay or coinsurance</li><li>Your out-of-pocket maximum</li>"
                               "<li>Whether your plan needs prior authorization</li><li>Any limit on the number of visits</li></ul>"),
            block("checklist", {"title": "Helpful to have ready", "color": "leaf", "items": [
                "Your insurance card",
                "Your child's doctor's name, so we can request a prescription (or a copy, if you already have one)",
                "Any evaluation from the last 6 months. It may mean your child can start right in therapy.",
                "Your child's IEP, if they get services at school",
            ]}),
            block("steps", {"heading": heading("From first call to first session", "How it works"), "steps": [
                {"title": "Call or text us", "text": "We'll gather your insurance and your child's doctor's information.", "link": link()},
                {"title": "Evaluation", "text": "Your child's therapist evaluates your child and talks with you about what they found.", "link": link()},
                {"title": "Plan of care", "text": "The therapist writes a plan of care and sends it to your pediatrician to sign. If your plan needs authorization, we request it next.", "link": link()},
                {"title": "Therapy begins", "text": "The whole process usually takes about two weeks. We'll call you to schedule as soon as it's done.", "link": link()},
            ]}),
            block("callout", {"color": "sky", "icon": "camera", "title": "Help your child know what to expect",
                              "text": "<p>Look through our first visit photo story together before you come. It shows the building, the front desk, the waiting room and the gym, one step at a time.</p>",
                              "button": link("See the photo story", first_visit)}),
            block("cta", {"color": "teal", "title": "Questions about coverage?",
                          "text": "Call or text 770-917-5737 and we'll walk you through it.",
                          "button": link("Contact us", contact), "secondary_button": link("Get started", get_started)}),
        )
        insurance.save_revision().publish()

        # ---------------- First visit photo story ----------------
        story_steps = [
            ("visit-01-building.jpg", "home", "This is Beyond Limits. This is where I go for therapy.", "The Beyond Limits building and sign"),
            ("visit-02-parking.jpg", "car", "We park the car and walk to the front door together.", "The parking lot and the path to the front door"),
            ("visit-03-door.jpg", "door", "This is the front door. We go inside.", "The clinic's front door"),
            ("visit-04-front-desk.jpg", "chat", "We say hello at the front desk. The people there are friendly.", "A smiling staff member at the front desk"),
            ("visit-05-waiting-room.jpg", "book", "I wait in the waiting room. I can read or play while I wait. Sometimes waiting takes a little while, and that's okay.", "The waiting room"),
            ("visit-06-hallway.jpg", "users", "My therapist comes to say hi. We walk down the hallway together.", "The hallway to the therapy rooms"),
            ("visit-07-bathroom.jpg", "toilet", "If I need the bathroom, it is right here. I can ask anytime.", "The bathroom"),
            ("visit-08-gym.jpg", "run", "We play and work in the gym. There are swings, mats and toys.", "A therapy gym with swings and mats"),
            ("visit-09-goodbye.jpg", "heart", "When we are done, I see my grown-up again. Then we go home. I did a great job!", "The front door from inside, on the way out"),
        ]
        first_visit.body = stream(
            block("visit_story", {
                "heading": "Your first visit, one step at a time",
                "parent_note": "Many children feel calmer when they know what will happen. Look through these pictures with your child a few times before the first visit and talk about each one. You can print them to keep at home or in the car.",
                "steps": [
                    {"type": "item", "value": {"photo": image_id(f, f"First visit: {alt} (starter photo)"), "icon": icon, "text": text, "alt": alt}, "id": str(uuid.uuid4())}
                    for f, icon, text, alt in story_steps
                ],
            }),
            block("callout", {"color": "leaf", "icon": "clipboard", "title": "Paperwork and insurance",
                              "text": "<p>What to bring, how we check your benefits, and how long it takes to get started.</p>",
                              "button": link("Insurance and your first visit", insurance)}),
        )
        first_visit.save_revision().publish()

        # ---------------- Resources ----------------
        resources.body = stream(
            block("paragraph", "<p>These organizations, materials and support programs help families of children with hearing loss and other developmental needs. Ask your child's therapist if you'd like recommendations.</p>"),
            block("links", {"heading": "Metro Atlanta", "links": [
                {"title": "Atlanta Area School for the Deaf", "url": "", "description": ""},
                {"title": "Atlanta Speech School", "url": "https://www.atlantaspeechschool.org/", "description": ""},
                {"title": "Auditory-Verbal Center of Atlanta", "url": "", "description": ""},
                {"title": "Babies Can't Wait", "url": "", "description": "Georgia's early intervention program for birth to 3"},
                {"title": "GA Hands & Voices", "url": "", "description": "Parent-to-parent support"},
                {"title": "GA PINES", "url": "", "description": ""},
            ]}),
            block("links", {"heading": "National organizations", "links": [
                {"title": "American Academy of Audiology", "url": "https://www.audiology.org/", "description": ""},
                {"title": "American Speech-Language-Hearing Association (ASHA)", "url": "https://www.asha.org/", "description": ""},
                {"title": "National Center for Hearing Assessment and Management", "url": "https://www.infanthearing.org/", "description": ""},
                {"title": "AG Bell", "url": "https://www.agbell.org/", "description": ""},
                {"title": "Hands & Voices", "url": "https://handsandvoices.org/", "description": ""},
                {"title": "John Tracy Center", "url": "https://www.jtc.org/", "description": "Free services for children with hearing loss up to age 5"},
            ]}),
            block("links", {"heading": "Family support and funding", "links": [
                {"title": "Georgia Council on Developmental Disabilities", "url": "https://gcdd.org/", "description": "Matching grants so family members can attend educational programs. Georgia residents, one grant per year."},
            ]}),
        )
        resources.save_revision().publish()

        # ---------------- Careers ----------------
        careers.body = stream(
            block("split", {
                "eyebrow": "Why Beyond Limits", "heading": "A place to grow your career, not just fill a caseload",
                "text": "<p>We're a team of audiologists, occupational therapists, physical therapists and speech-language pathologists who learn from each other every day. New grads and clinical fellows get real mentorship, and experienced clinicians get the space and support to do their best work.</p>"
                        "<p>And you'll see the difference you make. Over 750 kids come through our doors every week.</p>",
                "image": None, "illustration": "team", "image_side": "right", "button": link("See open roles", None, "#openings"),
            }),
            block("cards", {"heading": heading("What it's like here", "Life on the team"), "cards": [
                {"icon": "users", "color": "grape", "title": "Every discipline in one building", "text": "Walk down the hall to co-treat or ask a question.", "link": link()},
                {"icon": "grad", "color": "sky", "title": "Mentorship that's real", "text": "Support for new grads and CFs from experienced pediatric clinicians.", "link": link()},
                {"icon": "sparkle", "color": "coral", "title": "Space to do great therapy", "text": "Two therapy gyms, two sensory gyms and dedicated feeding rooms.", "link": link()},
                {"icon": "heart", "color": "leaf", "title": "Values we live by", "text": "Passion, discipline, transparency, accountability, teamwork and excellence.", "link": link()},
            ]}),
            block("team_teaser", {"heading": heading("Your future teammates", "Say hi"), "count": 8, "button": link("Meet the whole team", team)}),
            block("callout", {"color": "grape", "icon": "briefcase" if False else "star", "title": "Don't see your role?",
                              "text": "<p>We're always happy to hear from pediatric therapists. Send your resume and tell us what you love about working with kids.</p>",
                              "button": link()}),
        )
        careers.save_revision().publish()
        sample_job = JobPage(
            title="Pediatric Speech-Language Pathologist", slug="speech-language-pathologist", discipline="slp",
            employment_type="Full-time", location="Acworth, GA", hero_color="grape",
            summary="Example posting. Edit or unpublish before launch.",
            apply_email="info@blptc.org",
        )
        careers.add_child(instance=sample_job)
        sample_job.save_revision()  # left as a draft so editors have a template to copy

        # ---------------- Veterans ----------------
        veterans.body = stream(
            block("checklist", {"title": "Here for a VES appointment?", "color": "navy", "items": [
                "Bring your photo ID and your VES appointment details",
                "Plan on about an hour for a full hearing evaluation",
                "Results go back to VES within 24 to 48 hours",
            ]}),
            block("paragraph", "<p>Beyond Limits audiologists are honored to serve America's veterans and active-duty personnel with comprehensive hearing evaluations for members of the United States Armed Forces.</p>"
                               "<p>All of our audiologists are licensed by the State of Georgia and hold additional credentialing through VES to meet the specific needs of those who serve. Several are also credentialed to travel internationally, and recent trips have included Germany, Spain and Japan, where members of our Armed Forces are stationed.</p>"
                               "<p>If VES referred you to us, you'll receive a comprehensive audiological evaluation from a licensed audiologist, with results reported back to VES within 24 to 48 hours. We are honored to give back to those who have given so much.</p>"),
            block("cta", {"color": "sky", "title": "Questions about your appointment?", "text": "Call or text our front office and we'll help.",
                          "button": link("Contact us", contact), "secondary_button": link()}),
        )
        veterans.save_revision().publish()

        privacy.body = stream(
            block("callout", {"color": "sky", "icon": "shield", "title": "Placeholder",
                              "text": "<p>Paste the practice's Notice of Privacy Practices here before launch.</p>", "button": link()}),
        )
        privacy.save_revision().publish()

        self.stdout.write(self.style.SUCCESS(f"Seeded {Page.objects.count()} pages and {TeamMember.objects.count()} team members."))
