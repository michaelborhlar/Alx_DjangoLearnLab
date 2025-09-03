from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and hasattr(user, "profile") and user.profile.role == "Admin"

@user_passes_test(is_admin, login_url="/login/")
@login_required
def admin(request):
    return render(request, "admin_view.html")
    