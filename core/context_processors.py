import os


def site_flags(request):
    """Keep preview and staging copies of the site out of search engines."""
    return {"noindex": os.environ.get("SITE_NOINDEX", "") == "1"}
