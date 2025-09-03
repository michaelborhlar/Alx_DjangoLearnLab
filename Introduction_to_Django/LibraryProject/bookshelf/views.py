from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
# Create your views here.
@user_passes_test(is_admin, login_url="/login/")
@login_required
def admin(request):
    return render(request, "admin_view.html")
