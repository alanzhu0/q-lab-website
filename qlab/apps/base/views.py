from django.shortcuts import render

from .models import CarouselPhoto, ResearchPartner, Resource, Song, User
from ..projects.models import Project


def index(request):
    context = {"projects": Project.objects.all().order_by("-last_updated")[:7]}
    return render(request, "base/index.html", context=context)


def login(request):
    return render(request, "base/login.html")


def members(request, year=None):
    context = {
        "years": User.objects.filter(is_alumni=True).exclude(graduation_year__isnull=True).values_list("graduation_year", flat=True).distinct().order_by("graduation_year"),
        "year": year,
    }

    if year:
        context["students"] = [(u, u.project_set.all()) for u in User.objects.filter(graduation_year=year, is_alumni=True).order_by("first_name")]
    else:
        context["students"] = [(u, u.project_set.all()) for u in User.objects.filter(is_lab_student=True).order_by("graduation_year", "first_name")]

    return render(request, "base/members.html", context=context)


def partners(request):
    context = {"partners": ResearchPartner.objects.all()}
    return render(request, "base/partners.html", context=context)


def about_tour(request):
    context = {"photos": CarouselPhoto.objects.all()}
    return render(request, "base/about/tour.html", context=context)


def about_music(request):
    context = {"songs": Song.objects.all()}
    return render(request, "base/about/music.html", context=context)


def about_resources(request):
    context = {
        "learn": Resource.objects.filter(category="learn"),
        "articles": Resource.objects.filter(category="articles"),
        "comps": Resource.objects.filter(category="comps"),
        "opps": Resource.objects.filter(category="opps"),
    }
    return render(request, "base/about/resources.html", context=context)


def donate(request):
    return render(request, "base/donate.html")
