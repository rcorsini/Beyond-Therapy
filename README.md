# Beyond Limits Pediatric Therapy Center website

A Django + Wagtail rebuild of beyondlimitstherapy.org. The design takes the Beyond Limits brand (indigo and lime) and the playful feel of the "Little Ones" template, written as original code. None of the template's files are used.

## Who the site is for

1. **Families** of kids with developmental, sensory, motor, speech or hearing needs, many on the autism spectrum. Everything leads to "Start here".
2. **Therapists we want to hire.** They get a Careers page, a careers band on the home page, and a Careers link in the top bar.
3. **Veterans** with a VES hearing appointment. They're never more than one click away, through the top bar on every page, the mobile menu and the footer, but they aren't the focus.

## Run it locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_site          # starter pages, settings, team and profiles
python manage.py createsuperuser
python manage.py runserver
```

Open http://localhost:8000 for the site and http://localhost:8000/admin for the editor. To rebuild the starter content from scratch, run `python manage.py seed_site --reset`. This deletes all pages.

## What editors can change

- **Settings > Clinic settings**: logo, phone, fax, email, address, hours, map, social links, and which pages "Start here", Veterans, Careers and HIPAA link to.
- **Snippets > Team members**: providers and staff, with a photo, discipline, card blurb and full profile (licensure, education, experience). Each one gets a page at `/our-providers/<slug>/`.
- **Pages**: every page is built from blocks, including split text/image, card grids, numbered steps, checklists, FAQs, document lists, testimonials, stats, call-to-action banners and the form finder.
- **Home slider**: slides with an optional photo, caption box color and button. It rotates every 7 seconds, has a Pause button, and stops while hovered or focused. Visitors who prefer reduced motion get no auto-rotation.

## Page types

| Type | Used for |
| --- | --- |
| HomePage | Slider, numbered quick links, flexible body |
| StandardPage | About, Get Started, Resources, Veterans, HIPAA |
| ServiceIndexPage / ServicePage | Services and the four therapies |
| TeamPage | Providers, with a discipline filter and profile pages |
| CareersPage / JobPage | Careers and job postings (one sample posting is left as a draft) |
| ContactPage | Contact form with a map |

## Accessibility notes

- Text and buttons meet WCAG AA contrast. Lime buttons use dark text, and white text only sits on indigo, green or red.
- Motion respects `prefers-reduced-motion`. The slider can be paused, and the layout has no flashing or busy backgrounds.
- The site has a skip link, visible focus styles, an accessible mobile menu, and labeled form fields with inline errors.

## Before launch

- Upload the real logo, photos and PDF forms. The form finder shows "Ask us for this form" until a document is attached.
- Have each provider check their profile. These are lightly summarized from the developer's build (`core/fixtures/provider_profiles.json`).
- Work through the open questions in [`docs/client-questions.md`](docs/client-questions.md).
- Production settings read `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS` and `WAGTAILADMIN_BASE_URL` from the environment.
