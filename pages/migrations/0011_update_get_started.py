"""One-time update of an existing site's Get Started page to the redesigned form finder.

seed_site only fills an empty database, so this carries the October 2026 Get Started
content (the clinic's answers about each form, plus the new therapy and feeding forms)
to the Render preview. It publishes a new revision, so the old version stays in the
page's history. A fresh database has no pages yet and skips this; seed_site builds it.
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
    dependencies = [("pages", "0010_form_finder_pick_several"), ("home", "0008_form_finder_pick_several")]
    operations = [migrations.RunPython(update_get_started, migrations.RunPython.noop)]
