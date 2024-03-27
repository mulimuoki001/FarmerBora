from django.shortcuts import render,  redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from FarmerBora_App.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('home')
    else:
            form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def custom_logout(request):
    logout(request)
    # Redirect to a specific page after logging out
    messages.success(request, f'You have been logged out!')
    return HttpResponseRedirect(reverse('home'))
def index(request):
    return render(request, 'index.html')
def diseases(request):
    return render(request, 'diseases.html')
def forum(request):
    return render(request, 'forum.html')
def contact(request):
    return render(request, 'contact.html')
def playlist(request):
    return render(request, 'playlist.html')
def watchvideo(request):
    return render(request, 'watch-video.html')
def details(request):
    return render(request, 'details.html')
def posts(request):
    return render(request, 'posts.html')