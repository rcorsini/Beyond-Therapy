"""Republishes Get Started with the "now" and "before your first appointment" grouping.

After a phone call with the clinic (October 20, 2026): the speech, OT and PT Brief
Admissions forms are what new families used to get on a clipboard at the first
appointment, so new families now see them too, under "Before your first appointment".
Like 0011 and 0012, this rebuilds the page from seed_site and publishes a new revision
(the old one stays in the page's history); a fresh database skips it.
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
    dependencies = [("pages", "0014_form_item_stage"), ("home", "0009_form_item_stage")]
    operations = [migrations.RunPython(update_get_started, migrations.RunPython.noop)]
