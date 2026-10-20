"""Republishes Get Started as two doors: new patients, and patients adding therapies.

Russell's call with the clinic (October 20, 2026): every new patient starts with
General Admissions (and the Feeding Intake if needed); the therapies and their Brief
Admissions forms come after the first visit, or any time later, and that choice can be
opened straight from a front-desk QR code (/get-started/#adding). Like 0011, this
rebuilds the page from seed_site and publishes a new revision; a fresh database skips it.
"""

import json

from django.db import migrations


def update_get_started(apps, schema_editor):
    # The real models, because publishing needs Wagtail's revision methods.
    from wagtail.models import Page

    from core.management.commands.seed_site import get_started_blocks
    from pages.models import StandardPage

    page = StandardPage.objects.filter(slug="get-started").first()
    if not page:
        return
    pages = {p.slug: p for p in Page.objects.filter(slug__in=["insurance", "contact", "veterans"])}
    page.body = json.dumps(get_started_blocks(pages.get("insurance"), pages.get("contact"), pages.get("veterans")))
    page.save_revision().publish()


class Migration(migrations.Migration):
    dependencies = [("pages", "0016_form_finder_link_name"), ("home", "0010_form_finder_link_name")]
    operations = [migrations.RunPython(update_get_started, migrations.RunPython.noop)]
