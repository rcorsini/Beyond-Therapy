from django.urls import path
from wagtail import hooks

from .views import AddressCheckView


@hooks.register("register_admin_urls")
def register_address_check_url():
    # Wagtail wraps admin URLs so only signed-in staff can open them.
    return [path("address-check/", AddressCheckView.as_view(), name="address_check")]
