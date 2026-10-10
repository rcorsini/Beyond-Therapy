from django.views.generic import TemplateView
from wagtail.admin.views.generic.base import WagtailAdminTemplateMixin

from .security import client_ip

# Headers a proxy might put the visitor's address in, with REMOTE_ADDR last.
ADDRESS_HEADERS = [
    ("X-Forwarded-For", "HTTP_X_FORWARDED_FOR"),
    ("True-Client-IP", "HTTP_TRUE_CLIENT_IP"),
    ("CF-Connecting-IP", "HTTP_CF_CONNECTING_IP"),
    ("X-Real-IP", "HTTP_X_REAL_IP"),
    ("Connecting address (REMOTE_ADDR)", "REMOTE_ADDR"),
]


class AddressCheckView(WagtailAdminTemplateMixin, TemplateView):
    """Temporary, staff only: shows which address the login lockout sees, so
    core.security.client_ip can be checked on the real host. Remove once done."""

    page_title = "Address check"
    header_icon = "lock"
    template_name = "core/address_check.html"

    def get_breadcrumbs_items(self):
        return self.breadcrumbs_items + [{"url": "", "label": self.page_title}]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lockout_address"] = client_ip(self.request)
        context["headers"] = [(label, self.request.META.get(key, "")) for label, key in ADDRESS_HEADERS]
        return context
