from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm

# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You cacdn now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {"form": form})

# Profile View
@login_required
def profile(request):
    return render(request, "blog/profile.html")

