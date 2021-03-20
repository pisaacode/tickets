from django.contrib.auth.models import User
from functools import wraps
from django.http import HttpResponseRedirect

def is_login_redirect(redirect_url):

    def _login_redirect(func):
        @wraps(func)
        def _decorator(request, *args, **kwargs):
            if hasattr(request, 'user') and isinstance(request.user, User):
                return HttpResponseRedirect(redirect_url)
            else:
                return func(request, *args, **kwargs)

        return _decorator

    return _login_redirect