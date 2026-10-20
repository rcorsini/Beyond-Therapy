
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    # Replaces the original migration history, which databases created
    # before this squash have already applied.
    replaces = [("core", "0001_initial"), ("core", "0002_clinicsettings_insurance_page_and_more"), ("core", "0003_clinicsettings_first_visit_page")]

    initial = True

    dependencies = [
        ("wagtailcore", "0097_baselogentry_uuid_action_timestamp_indexes"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClinicSettings",
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
                    "clinic_name",
                    models.CharField(
                        default="Beyond Limits Pediatric Therapy Center", max_length=120
                    ),
                ),
                (
                    "short_name",
                    models.CharField(default="Beyond Limits", max_length=60),
                ),
                (
                    "tagline",
                    models.CharField(
                        blank=True,
                        default="Helping kids thrive, birth to 21.",
                        max_length=160,
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, help_text="Shown as 'Call or text'.", max_length=30
                    ),
                ),
                ("fax", models.CharField(blank=True, max_length=30)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("address_line_1", models.CharField(blank=True, max_length=120)),
                ("address_line_2", models.CharField(blank=True, max_length=120)),
                ("hours", models.CharField(blank=True, max_length=120)),
                (
                    "map_embed_url",
                    models.URLField(
                        blank=True,
                        help_text="Embed URL for the map on the contact page.",
                    ),
                ),
                ("directions_url", models.URLField(blank=True)),
                (
                    "veterans_label",
                    models.CharField(default="Veterans hearing exams", max_length=60),
                ),
                (
                    "secure_contact_url",
                    models.URLField(
                        blank=True,
                        help_text="Your HIPAA-secure contact form, for messages that include health details.",
                    ),
                ),
                ("facebook_url", models.URLField(blank=True)),
                ("instagram_url", models.URLField(blank=True)),
                ("youtube_url", models.URLField(blank=True)),
                ("linkedin_url", models.URLField(blank=True)),
                (
                    "careers_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "first_visit_page",
                    models.ForeignKey(
                        blank=True,
                        help_text="The photo walk-through of a first visit, linked from the footer, contact page and service pages.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "insurance_page",
                    models.ForeignKey(
                        blank=True,
                        help_text="Insurance and first-visit details, linked from the footer, contact page and service pages.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "logo",
                    models.ForeignKey(
                        blank=True,
                        help_text="The Beyond Limits logo. Without one, a simple placeholder mark is shown.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "privacy_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "start_page",
                    models.ForeignKey(
                        blank=True,
                        help_text="Where the 'Start here' button goes (usually Get Started).",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "veterans_page",
                    models.ForeignKey(
                        blank=True,
                        help_text="Linked from the top bar and footer so veterans always find it.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "Clinic settings",
            },
        ),
    ]
