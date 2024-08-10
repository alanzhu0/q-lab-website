from django.contrib.auth import get_user_model
from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(get_user_model())
    description = models.TextField(max_length=5000)
    last_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    poster_url = models.URLField(blank=True)
    presentation_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    paper_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def author_string(self):
        return ", ".join([u.display_name for u in self.authors.all()])

    def can_edit_or_post(self, user):
        return user in self.authors.all() or user.is_superuser

    def get_last_post(self):
        return self.post_set.all()[0]

    def has_info_urls(self):
        return self.poster_url or self.presentation_url or self.video_url or self.paper_url

    def info_urls(self):
        return {
            "Poster": self.poster_url,
            "Presentation": self.presentation_url,
            "Paper": self.paper_url,
            "Video": self.video_url,
        }


class Post(models.Model):
    id = models.AutoField(primary_key=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    content = models.TextField()


    class Meta:
        ordering = ("-last_updated",)


    def __str__(self):
        return f"Post on {self.last_updated} for {self.project} by {self.author}"


class Photo(models.Model):
    id = models.AutoField(primary_key=True)

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time_uploaded = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.FileField(upload_to="project_photos/")


    def __str__(self):
        return f"Photo for {self.project.title} (ID: {self.id})"

    def can_edit(self, user):
        return self.project.can_edit_or_post(user)
