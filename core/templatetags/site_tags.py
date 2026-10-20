"""Template helpers used across the site: icons, the main menu and small filters."""

from django import template
from django.utils.safestring import mark_safe

from wagtail.models import Site

register = template.Library()

# Original line icons, 24x24, drawn with stroke="currentColor".
ICONS = {
    "ear": '<path d="M7 9a5 5 0 0 1 10 0c0 3-3 4-3 7a3 3 0 0 1-5 2"/><path d="M10 9a2 2 0 0 1 4 0c0 1.5-2 2-2 3.5"/>',
    "hand": '<path d="M8 13V5.5a1.5 1.5 0 0 1 3 0V11"/><path d="M11 10V4.5a1.5 1.5 0 0 1 3 0V11"/><path d="M14 10.5V6a1.5 1.5 0 0 1 3 0v7a7 7 0 0 1-7 7h-.5a6 6 0 0 1-5-2.7L3 14.6a1.6 1.6 0 0 1 2.6-1.8L8 15"/>',
    "run": '<circle cx="14" cy="4.5" r="2"/><path d="M6 21l3.5-5.5L13 17l1 4"/><path d="M8 11l3-3.5 4 2 2.5 3.5"/><path d="M11 7.5l1.5 6.5"/>',
    "speech": '<path d="M4 5h16v10H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "puzzle": '<path d="M5 8h3a2 2 0 1 1 4 0h3v3a2 2 0 1 1 0 4v3h-3a2 2 0 1 0-4 0H5v-3a2 2 0 1 0 0-4z"/>',
    "family": '<circle cx="8" cy="6" r="2.5"/><circle cx="16" cy="6" r="2.5"/><circle cx="12" cy="13" r="2"/><path d="M4 21v-5a4 4 0 0 1 4-4M20 21v-5a4 4 0 0 0-4-4M9 21v-2a3 3 0 0 1 6 0v2"/>',
    "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 11h6M9 15h4"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "sparkle": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4"/><path d="M12 8l1.5 2.5L16 12l-2.5 1.5L12 16l-1.5-2.5L8 12l2.5-1.5z"/>',
    "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5M8 7h7"/>',
    "grad": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5M21 9v6"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-12 7l-5 1 1.5-4A8 8 0 1 1 21 12z"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
    "flag": '<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "doc": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 13h6M9 17h6"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14a5 5 0 0 1 5 5"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2M3 13h18"/>',
    "camera": '<rect x="3" y="6.5" width="18" height="13.5" rx="3"/><path d="M8.5 6.5L10 4h4l1.5 2.5"/><circle cx="12" cy="13" r="3.5"/>',
    "door": '<path d="M6 21V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v17"/><path d="M3 21h18"/><circle cx="14.5" cy="12.5" r="1"/>',
    "car": '<path d="M5 16V11l2-5h10l2 5v5"/><path d="M3 16h18v3H3z"/><circle cx="7.5" cy="13" r="1"/><circle cx="16.5" cy="13" r="1"/><path d="M6 19v2M18 19v2"/>',
    "toilet": '<path d="M6 3h5v8H6z"/><path d="M4 11h16a6 6 0 0 1-6 6h-4a6 6 0 0 1-6-6z"/><path d="M9 17l-1 4h8l-1-4"/>',
    "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
}


@register.simple_tag
def icon(name, size=24, label=""):
    """Inline SVG icon, e.g. {% icon "ear" 32 %}.

    Decorative (hidden from screen readers) unless a label is given. Unknown
    names fall back to the star.
    """
    paths = ICONS.get(name, ICONS["star"])
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return mark_safe(
        f'<svg class="icon icon-{name}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" {aria}>{paths}</svg>'
    )


@register.simple_tag(takes_context=True)
def main_menu(context):
    """Live, public top-level pages with "Show in menus" ticked, for the header nav."""
    request = context.get("request")
    site = Site.find_for_request(request) if request else None
    if not site:
        return []
    return site.root_page.get_children().live().public().in_menu().specific()


@register.simple_tag(takes_context=True)
def site_root(context):
    """The current site's home page."""
    request = context.get("request")
    site = Site.find_for_request(request) if request else None
    return site.root_page if site else None


@register.filter
def is_active(page, current):
    """True when `current` is `page` or below it, to highlight the menu item."""
    if not current or not getattr(current, "path", None):
        return False
    return current.path.startswith(page.path)


@register.filter
def split_lines(value):
    """Turn "one item per line" text into a list, skipping blank lines."""
    return [line.strip() for line in (value or "").splitlines() if line.strip()]
