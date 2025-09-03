from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


def is_librarian(user):
    return hasattr(user, "profile") and user.profile.role == 'Librarian'

@login_required(login_url="/login/")
@user_passes_test(is_librarian, login_url='/login/')

def librarian(request):
    return render(request, 'librarian_view.html')
