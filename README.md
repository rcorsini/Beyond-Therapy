# Beyond Limits Pediatric Therapy Center website

A Django + Wagtail rebuild of [beyondlimitstherapy.org](https://beyondlimitstherapy.org/), the site of a pediatric therapy clinic in Acworth, Georgia (audiology, occupational, physical and speech-language therapy, birth to 21).

The look takes the Beyond Limits brand (indigo `#45488f` and lime `#8dc63f`) and the playful feel of the "Little Ones" ThemeForest template, but **all code, CSS, illustrations and icons here are original**. None of the template's files are used, and none should be added: the project has no license to them.

- **Preview:** https://beyond-limits-preview.onrender.com (editor at `/admin/`)
- **Architecture and code tour:** [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- **Open questions for the clinic:** [`docs/client-questions.md`](docs/client-questions.md)

## Who the site is for

In priority order:

1. **Families** of kids with developmental, sensory, motor, speech or hearing needs, many on the autism spectrum. Everything leads to "Start here" (the Get Started page).
2. **Therapists the clinic wants to hire.** They get a Careers page, a careers band and a hiring slide on the home page, and a Careers link in the top bar.
3. **Veterans** coming for a VES hearing exam. They're never more than one click away (top bar on every page, mobile menu, footer) but they aren't the focus.

Accessibility is a requirement, not a nice-to-have: see [Accessibility](#accessibility).

## Quick start (local)

Needs Python 3.12 (the version Render uses; 3.11+ should work). Locally SQLite is the database, so nothing else to install; set `DATABASE_URL` to use Postgres instead, as Render does.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_site          # starter pages, settings, providers and photos
python manage.py createsuperuser
python manage.py runserver
```

Open http://localhost:8000 for the site and http://localhost:8000/admin/ for the Wagtail editor.

`manage.py` uses `beyondlimits.settings.dev` by default (debug on, any host allowed, email printed to the console). For machine-specific overrides, create `beyondlimits/settings/local.py`; it's imported last by both settings files and is git-ignored.

### Tests

```bash
python manage.py test
```

The tests (`core/tests/test_site.py`) seed the site and then check that every page type renders, the Veterans link is on every page, the contact form behaves correctly with and without LuxSci, and the admin login lockout works. Run them, and `python manage.py makemigrations --check`, before every push.

## Starter content: `seed_site`

`core/management/commands/seed_site.py` builds the whole site from code: the page tree, every page's blocks, the clinic settings, all providers and the starter photos. It's what makes the site usable straight after `migrate`, and it filled the Render preview's database the first time it started.

```bash
python manage.py seed_site          # does nothing if a HomePage already exists
python manage.py seed_site --reset  # deletes ALL pages and providers, then rebuilds
```

`--reset` is destructive: it deletes every page under the root, every provider, and every image whose title ends in "(starter photo)". Never run it against a database with real edits you want to keep.

Where the content comes from:

- **Page copy** is adapted from beyondlimitstherapy.org and from the clinic's developer's WordPress build. It lives inline in `seed_site.py`, one section per page (search for `# ---------------- About`, etc.).
- **Provider list** is the `PROVIDERS` table near the top of `seed_site.py` (name, credentials, title, discipline, clinician or office staff).
- **Provider profiles** (intro, licensure, education, experience) are in `core/fixtures/provider_profiles.json`, keyed by the provider's name. They're summarized from the developer's build, and each provider still needs to review theirs.
- **Starter photos** are in `core/seed_images/`. See [`core/seed_images/README.md`](core/seed_images/README.md) for which file goes where. A missing file is simply skipped and that spot falls back to its illustration or icon, so photos can be added one at a time.
  - **Provider headshots** go in `core/seed_images/providers/<slug>.jpg`, where `<slug>` is the end of the provider's profile address (`kimberly-oviedo.jpg` for `/our-providers/kimberly-oviedo/`). Tall photos get a focal point on their upper third so the face survives the square crop. Use 800px wide or more.
  - **Strip phone metadata (GPS) before committing a photo.** One original already carried a location.
  - Credits for the stock photos are in `core/seed_images/CREDITS.md`. Patient photos need a signed parent photo release; the hiring slide and the first-visit photo story use the clinic's own photos only, never stock.

## Preview on Render

`render.yaml` is a Render Blueprint for a preview that redeploys on every push to `feature/wagtail-site`: a $7 web service, a $6 Render Postgres database and a 1 GB persistent disk for uploads ($0.25), about $13.25 a month. To set one up: in Render choose **New > Blueprint**, pick this repository and branch, and enter an admin username, email and password when asked. Change plans in `render.yaml`, not the Render dashboard, or the Blueprint can change them back.

On each start the service runs `migrate`, then `seed_site`, then `createsuperuser` (from the `DJANGO_SUPERUSER_*` variables), then gunicorn.

Pages live in Postgres and uploads on the disk (`MEDIA_ROOT=/var/data/media`), so edits made in the admin survive deploys. `seed_site` only fills an empty database, so later changes to the seed data don't reach the existing preview; add that content in the admin instead. The admin login from the environment is created once; after that, change the password in the admin. Because of the disk, each deploy has a short gap while the old copy stops.

The preview sends `noindex` to search engines (`SITE_NOINDEX=1`).

## Environment variables

Production settings (`beyondlimits.settings.production`) read:

| Variable | Required | What it does |
| --- | --- | --- |
| `DJANGO_SETTINGS_MODULE` | yes | `beyondlimits.settings.production` on any real server. |
| `DJANGO_SECRET_KEY` | yes | Django secret key. Render generates one. |
| `DJANGO_ALLOWED_HOSTS` | yes, off Render | Comma-separated hostnames. On Render, `RENDER_EXTERNAL_HOSTNAME` is added automatically. CSRF trusted origins are derived from this list. |
| `WAGTAILADMIN_BASE_URL` | no | Full site URL for links in admin emails. Defaults to the Render hostname. |
| `SITE_NOINDEX` | no | `1` adds a `noindex` robots tag to every page. Set on previews; never on the live site. |
| `DATABASE_URL` | Render sets it | Postgres connection string. Without it, SQLite is used. |
| `SQLITE_PATH` | no | Where the SQLite file lives when there's no `DATABASE_URL`. Defaults to `db.sqlite3` in the repo root. |
| `MEDIA_ROOT` | Render sets it | Folder for uploaded images and documents. On Render it's the persistent disk. Defaults to `media/` in the repo root. |
| `SERVE_MEDIA` | no | `1` (default) lets Django serve `/media/` itself when debug is off. Set `0` if media ever moves to S3 or similar. |
| `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`, `DEFAULT_FROM_EMAIL` | no | SMTP for the fallback Wagtail contact form. Without `EMAIL_HOST`, mail is written to the log instead. Not used while the LuxSci form is on. |
| `DJANGO_SUPERUSER_USERNAME`, `_EMAIL`, `_PASSWORD` | Render only | The first admin login, created when the database is new. |

There's also a `Dockerfile` (the Wagtail project default, lightly used) if you'd rather run it in a container.

## How editors use the Wagtail admin

Editors log in at `/admin/`. What they can change:

- **Pages** (left menu): every page is built from content blocks such as headings, rich text, split text/image, card grids, numbered steps, checklists, callouts, FAQs, link and document lists, testimonials, stats, call-to-action banners, the forms chooser, the first-visit photo story and the "Does this sound like your child?" cards. Each page also has a header intro line and color.
- **Home page slider**: slides with a photo (or an illustration), caption box color, button and note. It rotates every 7 seconds with a checkerboard tile transition, has a Pause button, stops on hover or focus, and doesn't auto-rotate for visitors who prefer reduced motion.
- **Providers** (left menu, under Pages): add, edit, reorder and remove providers and office staff. Each has a photo, discipline, card blurb and full profile (licensure, education, experience), and gets a page at `/our-providers/<slug>/`. Untick **Clinician** for front office staff (they're listed but left out of the home page team row).
- **Settings > Clinic settings**: logo, phone, fax, email, address, hours, map, social links, and which pages "Start here", Veterans, Careers, HIPAA, Insurance and First visit link to.
- **Images**: set a **focal point** on any photo whose crop cuts off faces. Slides, service photos and headshots are cropped square; first-visit photos to 4:3. The Our Providers team photo is never cropped. Fill in each image's description for screen readers.
- **Contact page**: the "LuxSci Secure Form code" field. See [Contact form](#contact-form-luxsci).

### Contact form (LuxSci)

The Contact Us form posts **straight to LuxSci** (a HIPAA-compliant form service), not to this server, so messages that mention a child's health are never saved in the admin or written to logs. Its form code (currently `18249-26830-Zg4g`) is set on the Contact page in the admin. While it's set, the page refuses any POST to itself.

After sending, LuxSci should send families back to `/contact/?sent=1`, which shows the thank-you text. That redirect is set in LuxSci's own settings, not here.

Clearing the code falls back to a normal Wagtail form that saves submissions in the admin and emails them. Only do that if no health details will ever come through it.

The forms on Get Started are separate LuxSci forms the clinic already uses, linked by URL: the older ones at `secureform.luxsci.com/forms/18016/...` and the newer Brief Admissions and Feeding Intake forms (October 2026, LuxSci account 18249) at `beyond-limits.secure-form.com/...`. Their wording lives in `get_started_blocks()` in `seed_site.py`; on the live site, edit them on the Get Started page in the admin.

### Admin login lockout

[django-axes](https://django-axes.readthedocs.io/) locks a username + visitor address pair for one hour after 5 wrong passwords. There's no unlock screen in the admin; from a shell on the server run `python manage.py axes_reset` (or `axes_reset_username <name>`). The visitor address comes from Cloudflare's header on Render; see `core/security.py` and the architecture doc before moving hosts.

## Accessibility

- Target is WCAG 2.1 AA. The owner checks pages with WAVE; axe reports zero A/AA violations on all page types. Keep it that way: check WAVE and axe after any template or CSS change.
- When running axe, turn on reduced motion. Otherwise scroll-reveal elements are caught mid-fade and read as low contrast.
- Text and buttons meet AA contrast. Lime buttons use dark text; white text only sits on indigo, green or red. Lime text on indigo fails.
- All motion respects `prefers-reduced-motion`. The slider can be paused; page-header butterflies play once in under 5 seconds (WCAG 2.2.2).
- Skip link, visible focus styles, an accessible mobile menu, labeled form fields, one `h1` per page, and headings in order.
- Manual keyboard and screen-reader testing is still recommended before launch.

## Before launch

Launch blockers:

- [ ] **HIPAA Privacy Policy page** is a placeholder. The clinic must supply the real notice.
- [ ] **Remove `SITE_NOINDEX`** on the live site, and set `DJANGO_ALLOWED_HOSTS` / `WAGTAILADMIN_BASE_URL` for the real domain.
- [ ] **Sample job posting**: `seed_site` creates an example Speech-Language Pathologist posting that is meant to be a draft but is published (live) on the Careers page. Unpublish or replace it.
- [ ] **Login lockout address**: if the live host isn't behind Cloudflare, update `core/security.py` (see its docstring).

Waiting on the clinic:

- [ ] **Photos**: real team photo (replaces the stand-in on Our Providers, which shows another organization's wall sign), clinic photos for the first-visit story and hiring slide, more provider headshots. A shot list was sent.
- [ ] **High-resolution logo** (SVG, AI, EPS, or PNG 1000px+). The current file is 175px wide.
- [ ] **Provider profiles** reviewed by each provider.
- [ ] **New forms**: confirm with the clinic how Get Started uses the four new forms (speech, OT and PT Brief Admissions, Feeding Intake), listed in `docs/client-questions.md`.
- [ ] **LuxSci**: confirm form account 18249 (contact) belongs to the clinic under its HIPAA agreement (the admission forms use 18016), and set its after-send page to `/contact/?sent=1`.
- [ ] **Slide wording** confirmed by the clinic.

Nice to have:

- [ ] Two-factor login for the admin.
- [ ] Manual keyboard and screen-reader pass.
