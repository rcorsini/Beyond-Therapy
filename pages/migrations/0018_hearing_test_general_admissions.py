"""Republishes Get Started with General Admissions first on the hearing-test path.

Russell's answer (October 20, 2026): a hearing test starts with General Admissions, like
every new patient, then the Audiology Admission Form. Like 0011, this rebuilds the page from
seed_site and publishes a new revision; a fresh database skips it.
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
    dependencies = [("pages", "0017_get_started_two_doors")]
    operations = [migrations.RunPython(update_get_started, migrations.RunPython.noop)]
