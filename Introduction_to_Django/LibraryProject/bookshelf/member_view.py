from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_member(user):
    return hasattr(user, "profile") and user.profile.role == "Member"


@login_required(login_url="/login/")
@user_passes_test(is_member, login_url="/login/")
def member(request):
    return render(request, "member_view.html")