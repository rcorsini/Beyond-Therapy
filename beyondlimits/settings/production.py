from .base import *

DEBUG = False

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = [h.strip() for h in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",") if h.strip()]
# Render sets this to the service's own onrender.com hostname.
if os.environ.get("RENDER_EXTERNAL_HOSTNAME"):
    ALLOWED_HOSTS.append(os.environ["RENDER_EXTERNAL_HOSTNAME"])
    WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL", f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}")
CSRF_TRUSTED_ORIGINS = [f"https://{h}" for h in ALLOWED_HOSTS]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# WhiteNoise serves the hashed, compressed static files straight from the app,
# so no separate static host is needed.
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

try:
    from .local import *
except ImportError:
    pass
