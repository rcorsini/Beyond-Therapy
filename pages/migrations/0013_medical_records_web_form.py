"""Links the new secure Medical Records web form on an existing Get Started page.

The clinic replaced its Medical Records PDF with a LuxSci form (October 2026). This
only fills in that one form's link, so other admin edits to the page are kept, and
publishes a new revision. A fresh database skips it; seed_site builds the page.
"""

import json

from django.db import migrations

URL = "https://beyond-limits.secure-form.com/medical-records/"


def items(values):
    """A ListBlock's values: seeded as plain dicts, saved by the admin as {"type": "item", "value": ...}."""
    return [v["value"] if v.get("type") == "item" else v for v in values]


def link_records_form(apps, schema_editor):
    from pages.models import StandardPage  # the real model, for Wagtail's revision methods

    page = StandardPage.objects.filter(slug="get-started").first()
    if not page:
        return
    body = page.body.get_prep_value()
    changed = False
    for block in body:
        if block["type"] != "form_finder":
            continue
        for path in items(block["value"]["paths"]):
            for opt in items(path["options"]):
                for f in items(opt["forms"]):
                    if f["title"].startswith("Medical Records") and not f.get("online_url"):
                        f["online_url"] = URL
                        changed = True
    if changed:
        page.body = json.dumps(body)
        page.save_revision().publish()


class Migration(migrations.Migration):
    dependencies = [("pages", "0012_get_started_brief_forms")]
    operations = [migrations.RunPython(link_records_form, migrations.RunPython.noop)]
