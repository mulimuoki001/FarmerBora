from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import create_post, update_profile, latest_post_data

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", views.custom_logout, name="logout"),
    path("index/", views.index, name="index"),
    path("diseases/", views.diseases, name="diseases"),
    path("forum/", views.forum, name="forum"),
    path("contact/", views.contact, name="contact"),
    path("playlist", views.playlist, name="playlist"),
    path("watch-video", views.watchvideo, name="watch-video"),
    path("posts/<slug>/", views.posts, name="posts"),
    path("details/<slug>/", views.details, name="details"),
    path("create_post/", create_post, name="create_post"),
    path("update_profile/", update_profile, name="update_profile"),
    path("latest_post_data/", latest_post_data, name="latest_post_data"),
]
