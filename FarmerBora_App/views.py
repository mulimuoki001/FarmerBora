from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from FarmerBora_App.forms import UserRegistrationForm, PostForm, UpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Category, Author, CustomUser, Comment, Reply
from .utils import update_views
import pusher
from django.conf import settings
from django.http import JsonResponse


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
    forums = Category.objects.all()
    context = {"forums": forums}
    return render(request, "forum.html", context)


def contact(request):
    return render(request, "contact.html", {"request": request})


def playlist(request):
    return render(request, "playlist.html", {"request": request})


def watchvideo(request):
    return render(request, "watch-video.html", {"request": request})


def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    author = Author.objects.get(user=request.user)

    if request.method == "POST":
        if "comment-form" in request.POST:
            comment = request.POST.get("comment")
            new_comment, created = Comment.objects.get_or_create(
                user=author, content=comment, post=post
            )
            post.comments.add(new_comment)
        elif "reply-form" in request.POST:
            reply = request.POST.get("reply")
            comment_id = request.POST.get("comment-id")
            comment_obj = Comment.objects.get(id=comment_id)
            new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
            comment_obj.replies.add(new_reply)

    context = {
        "post": post,
    }
    update_views(request, post)
    return render(request, "details.html", context)


def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    context = {
        "posts": posts,
        "forum": category,
    }
    return render(request, "posts.html", context)


@login_required
def update_profile(request):
    context = {}
    user = request.user

    if Author.objects.filter(user=user).exists():
        messages.warning(request, "You are already an author.")
        return redirect("forum")  # Redirect to the forum if already an author

    form = UpdateForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect("forum")
    context.update({"form": form, "title": "Update Profile"})
    return render(request, "update_profile.html", context)


@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            pusher_client = pusher.Pusher(
                app_id=settings.PUSHER_APP_ID,
                key=settings.PUSHER_KEY,
                secret=settings.PUSHER_SECRET,
                cluster=settings.PUSHER_CLUSTER,
            )
            pusher_client.trigger(
                "my-channel", "new-post", {"message": "A new post has been created!"}
            )

            return redirect("forum")
    context.update({"form": form, "title": "Create New  Post"})

    return render(request, "create_post.html", context)


def latest_post_data(request):
    try:
        current_user = request.user
        latest_post = Post.objects.latest("date")
        post_data = {
            "title": latest_post.title,
            "user": latest_post.user.fullname,
            "current_user_name": current_user.username,
        }
        return JsonResponse(post_data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
