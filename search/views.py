from django.core.paginator import Paginator
from django.template.response import TemplateResponse

from wagtail.models import Page


def search(request):
    """Site search over live pages, ten results a page (?query=...&page=...)."""
    search_query = request.GET.get("query")
    results = Page.objects.live().search(search_query) if search_query else Page.objects.none()
    # get_page falls back to the first page for a bad number and the last page for one too high.
    search_results = Paginator(results, 10).get_page(request.GET.get("page"))
    return TemplateResponse(request, "search/search.html", {"search_query": search_query, "search_results": search_results})
