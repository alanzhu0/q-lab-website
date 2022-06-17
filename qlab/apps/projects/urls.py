from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


app_name = "projects"

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("detail/<int:project_id>/", views.project_detail, name="project_detail"),
    path("edit/<int:project_id>/", views.project_edit, name="project_edit"),
    path("post/add/<int:project_id>/", views.post_add, name="post_add"),
    path("post/edit/<int:project_id>/<int:post_id>/", views.post_edit, name="post_edit"),
]
