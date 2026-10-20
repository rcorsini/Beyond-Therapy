"""Republishes Get Started once the new LuxSci forms could be read (October 2026).

The speech, OT and PT Brief Admissions forms are for children who already come here,
so they move to the "adding a therapy" path; new patients fill out General Admissions,
plus the Feeding Intake for feeding concerns. Like 0011, it publishes a new revision
(the old version stays in the page's history) and skips a fresh database.
"""

import json

from django.db import migrations


def update_get_started(apps, schema_editor):
    # The real models, because publishing needs Wagtail's revision methods.
    from wagtail.models import Page

    from core.management.commands.seed_site import GET_STARTED_INTRO, get_started_blocks
    from pages.models import StandardPage

    page = StandardPage.objects.filter(slug="get-started").first()
    if not page:
        return
    pages = {p.slug: p for p in Page.objects.filter(slug__in=["insurance", "contact", "veterans"])}
    page.body = json.dumps(get_started_blocks(pages.get("insurance"), pages.get("contact"), pages.get("veterans")))
    page.hero_intro = GET_STARTED_INTRO
    page.save_revision().publish()


class Migration(migrations.Migration):
    dependencies = [("pages", "0011_update_get_started")]
    operations = [migrations.RunPython(update_get_started, migrations.RunPython.noop)]
