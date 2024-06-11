from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


app_name = "base"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("members/", views.members, name="members"),
    path("members/<int:year>/", views.members, name="members"),
    path("partners/", views.partners, name="partners"),
    path("about/tour/", views.about_tour, name="about_tour"),
    path("about/music/", views.about_music, name="about_music"),
    path("about/resources/", views.about_resources, name="about_resources"),
    path("donate/", views.donate, name="donate"),
]
