def client_ip(request):
    """The visitor's address for login lockout.

    On Render the app sits behind a proxy, so REMOTE_ADDR is the proxy. This
    uses the last X-Forwarded-For entry because earlier entries can be faked by
    the visitor. Render may append its own proxy address there, which would
    make lockout per username instead of per username and address. That fails
    safe (no extra guesses), but it hasn't been checked on Render yet: open
    /admin/address-check/ on the live site to see which header holds the
    visitor's real address, then switch to it here.
    """
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if forwarded:
        return forwarded.split(",")[-1].strip()
    return request.META.get("REMOTE_ADDR")
