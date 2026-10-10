def client_ip(request):
    """The visitor's address for login lockout.

    On Render the app sits behind a proxy, so REMOTE_ADDR is the proxy. The
    proxy adds the address that connected to it at the end of X-Forwarded-For;
    earlier entries can be faked by the visitor, so only the last one is used.
    If that turns out to be another proxy, lockout still works, just per
    username instead of per username and address.
    """
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if forwarded:
        return forwarded.split(",")[-1].strip()
    return request.META.get("REMOTE_ADDR")
