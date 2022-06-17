from django.contrib.auth import get_user_model
from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(get_user_model())
    description = models.TextField(max_length=5000)
    last_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    def author_string(self):
        return ", ".join([str(u) for u in self.authors.all()])

    def can_edit_or_post(self, user):
        return user in self.authors.all() or user.is_superuser

    def get_last_post(self):
        return self.post_set.all()[0]


class Post(models.Model):
    id = models.AutoField(primary_key=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    content = models.TextField(max_length=5000)


    class Meta:
        ordering = ("-last_updated",)


    def __str__(self):
        return f"Post on {self.last_updated} for {self.project} by {self.author}"
