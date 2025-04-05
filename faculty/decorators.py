from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.role != role:
                return HttpResponseForbidden("Access denied. You are not authorized.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
