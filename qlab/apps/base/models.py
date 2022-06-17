from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)

    graduation_year = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    is_alumni = models.BooleanField(default=False)
    is_lab_student = models.BooleanField(default=False)

    picture = models.FileField(upload_to="student_photos/", blank=True, null=True)

    class Meta:
        ordering = ("last_name", "first_name")

    def get_social_auth(self):
        return self.social_auth.get(provider="ion")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ResearchPartner(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    picture = models.FileField(upload_to="partner_photos/")

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return f"{self.title} by {self.artist_name}"
