from django.contrib import admin

from .models import Photo, Project, Post


@admin.action(description="Mark inactive")
def mark_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


class ProjectAdmin(admin.ModelAdmin):
    actions = [mark_inactive]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Post)
admin.site.register(Photo)
