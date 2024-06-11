from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PhotoForm, PostForm, ProjectEditForm
from .models import Photo, Post, Project
from ..base.models import User


def project_list(request, year=None):
    context = {
        "years": User.objects.filter(is_alumni=True).exclude(graduation_year__isnull=True).values_list("graduation_year", flat=True).distinct().order_by("graduation_year"),
        "year": year,
    }
    if year:
        context["projects"] = Project.objects.filter(authors__graduation_year=year, authors__is_alumni=True).distinct().order_by("-active", "-last_updated")
    else:
        context["projects"] = Project.objects.filter(authors__is_lab_student=True).distinct().order_by("-active", "-last_updated")
    return render(request, "projects/list.html", context=context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        "editor": project.can_edit_or_post(request.user),
        "project": project,
        "posts": project.post_set.all(),
        "photos": project.photo_set.all(),
    }

    return render(request, "projects/detail.html", context=context)


@login_required
def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if project.can_edit_or_post(request.user):
        form = ProjectEditForm(instance=project)

        if request.method == "POST":
            form = ProjectEditForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect(reverse("projects:project_detail", args=[project.id]))
        
        return render(request, "projects/edit.html", context={"form": form})
    else:
        raise PermissionDenied


@login_required
def post_add(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if project.can_edit_or_post(request.user):
        form = PostForm()

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = Post.objects.create(
                    project=project,
                    author=request.user,
                    content=form.cleaned_data["content"],
                )
                project.save()
                return redirect(reverse("projects:project_detail", args=[project.id]))
        
        return render(request, "projects/post.html", context={"action": "Add", "project": project, "form": form})
    else:
        raise PermissionDenied


@login_required
def post_edit(request, project_id, post_id):
    project = get_object_or_404(Project, id=project_id)
    post = get_object_or_404(Post.objects.filter(project=project), id=post_id)

    if project.can_edit_or_post(request.user):
        form = PostForm(initial={"content": post.content})

        if request.method == "POST":
            if "button-save" in request.POST:
                form = PostForm(request.POST)
                if form.is_valid():
                    post.content = form.cleaned_data["content"]
                    post.save()
                    project.save()
                    return redirect(reverse("projects:project_detail", args=[project.id]))
            elif "button-delete" in request.POST:
                post.delete()
                return redirect(reverse("projects:project_detail", args=[project.id]))
        
        return render(request, "projects/post.html", context={"action": "Edit", "project": project, "form": form})
    else:
        raise PermissionDenied


@login_required
def photo_add(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if project.can_edit_or_post(request.user):
        form = PhotoForm()

        if request.method == "POST":
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                photo = Photo.objects.create(
                    project=project,
                    owner=request.user,
                    image=form.cleaned_data["image"],
                )
                project.save()
                return redirect(reverse("projects:project_detail", args=[project.id]))
        
        return render(request, "projects/photo.html", context={"project": project, "form": form})
    else:
        raise PermissionDenied
