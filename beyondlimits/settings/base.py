"""Settings shared by dev.py (local) and production.py (Render and launch)."""

import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = PROJECT_DIR.parent

INSTALLED_APPS = [
    "core",
    "home",
    "pages",
    "search",
    "wagtail.contrib.settings",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django_filters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "axes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    # Last, as django-axes asks.
    "axes.middleware.AxesMiddleware",
]

# Admin login lockout (django-axes): after 5 wrong passwords for the same
# username from the same address, that pair is locked out for an hour.
# There is no screen for unlocking early: django-axes adds nothing to the
# Wagtail admin. Either wait the hour or run `manage.py axes_reset` (or
# `axes_reset_username <name>`) from a shell on the server.
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesStandaloneBackend",
    "django.contrib.auth.backends.ModelBackend",
]
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1  # hours
AXES_LOCKOUT_PARAMETERS = [["username", "ip_address"]]
AXES_RESET_ON_SUCCESS = True
AXES_CLIENT_IP_CALLABLE = "core.security.client_ip"

ROOT_URLCONF = "beyondlimits.urls"
WSGI_APPLICATION = "beyondlimits.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
                "core.context_processors.site_flags",
            ],
        },
    },
]

# Postgres when the host provides DATABASE_URL (Render does, from the database
# in render.yaml); otherwise a local SQLite file.
if os.environ.get("DATABASE_URL"):
    import dj_database_url

    DATABASES = {"default": dj_database_url.parse(os.environ["DATABASE_URL"], conn_max_age=600, conn_health_checks=True)}
    # Wagtail's search index uses Postgres full-text search, which needs this app.
    INSTALLED_APPS.append("django.contrib.postgres")
else:
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": os.environ.get("SQLITE_PATH", BASE_DIR / "db.sqlite3")}}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"django.contrib.auth.password_validation.{name}"}
    for name in ("UserAttributeSimilarityValidator", "MinimumLengthValidator", "CommonPasswordValidator", "NumericPasswordValidator")
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_TZ = True

# CSS, JavaScript and images that ship with the code. collectstatic gathers them into STATIC_ROOT.
STATICFILES_DIRS = [PROJECT_DIR / "static"]
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

# Uploaded images and documents. On Render this points at the persistent disk
# (see render.yaml), since the rest of the server's files are wiped on each deploy.
MEDIA_ROOT = os.environ.get("MEDIA_ROOT", BASE_DIR / "media")
MEDIA_URL = "/media/"
# Let Django serve uploads when no web server or file host sits in front of it.
SERVE_MEDIA = os.environ.get("SERVE_MEDIA", "1") == "1"

# Complex pages can have more than Django's default of 1000 fields in Wagtail's page editor.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10_000

WAGTAIL_SITE_NAME = "Beyond Limits Pediatric Therapy Center"
WAGTAILSEARCH_BACKENDS = {"default": {"BACKEND": "wagtail.search.backends.database"}}
# Full site URL for links in admin emails, without /admin or a trailing slash.
WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL", "http://localhost:8000")
# File types editors may upload as documents, up to 10 MB each.
WAGTAILDOCS_EXTENSIONS = ["csv", "docx", "key", "odt", "pdf", "pptx", "rtf", "txt", "xlsx", "zip"]
WAGTAILDOCS_MAX_UPLOAD_SIZE = 10 * 1024 * 1024
