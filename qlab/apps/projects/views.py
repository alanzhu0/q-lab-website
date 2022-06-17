from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PostForm, ProjectEditForm
from .models import Post, Project


def project_list(request):
    context = {"projects": Project.objects.all().order_by("-active", "-last_updated")}
    return render(request, "projects/list.html", context=context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        "project": project,
        "posts": project.post_set.all(),
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
