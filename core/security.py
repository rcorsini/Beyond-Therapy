def client_ip(request):
    """The visitor's address for login lockout.

    On Render a request passes through Cloudflare, then Render's proxy, so
    REMOTE_ADDR and the last X-Forwarded-For entry are Render's own addresses
    (checked on the preview, 2026-10-10). Cloudflare puts the address that
    connected to it in CF-Connecting-IP and True-Client-IP, replacing anything
    the visitor sent, so those can't be faked. Earlier X-Forwarded-For entries
    can be, so they're never used.

    If the site moves to a host that isn't behind Cloudflare, those two headers
    could be faked there: drop them and check what the new host sends.
    """
    for header in ("HTTP_CF_CONNECTING_IP", "HTTP_TRUE_CLIENT_IP"):
        address = request.META.get(header, "").strip()
        if address:
            return address
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if forwarded:
        return forwarded.split(",")[-1].strip()
    return request.META.get("REMOTE_ADDR")
