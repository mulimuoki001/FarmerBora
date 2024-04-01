from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from FarmerBora_App.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging


def home(request):
    return render(request, "home.html")


def register(request):
    form = None
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile_picture = form.cleaned_data.get("profile_picture")
            if profile_picture:
                user.profile_picture = profile_picture
                user.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created successfully for {username}!")
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def profile(request):
    return render(request, "profile.html")


def custom_logout(request):
    logout(request)
    # Redirect to a specific page after logging out

    messages.success(request, f" You have been logged out!")
    return HttpResponseRedirect(reverse("home"))


def index(request):
    return render(request, "index.html", {"request": request})


def diseases(request):
    return render(request, "diseases.html", {"request": request})


def forum(request):
    return render(request, "forum.html", {"request": request})


def contact(request):
    return render(request, "contact.html", {"request": request})


def playlist(request):
    return render(request, "playlist.html", {"request": request})


def watchvideo(request):
    return render(request, "watch-video.html", {"request": request})


def details(request):
    return render(request, "details.html")


def posts(request):
    return render(request, "posts.html")
