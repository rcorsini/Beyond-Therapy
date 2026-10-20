from wagtail.admin.ui.tables import BooleanColumn
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import TeamMember


class ProviderViewSet(SnippetViewSet):
    """Gives providers their own item in the admin menu instead of hiding them under Snippets."""

    model = TeamMember
    icon = "group"
    menu_label = "Providers"
    menu_name = "providers"
    menu_order = 150
    add_to_admin_menu = True
    list_display = ["name", "credentials", "title", "discipline", BooleanColumn("is_clinician", label="Clinician")]
    list_filter = ["discipline", "is_clinician"]
    ordering = ["sort_order", "name"]


register_snippet(ProviderViewSet)
