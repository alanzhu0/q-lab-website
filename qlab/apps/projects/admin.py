from django.contrib import admin

from .models import Photo, Project, Post


@admin.action(description="Mark inactive")
def mark_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


class ProjectAdmin(admin.ModelAdmin):
    def project_year(obj):
        return obj.authors.first().graduation_year

    list_display = ("title", "author_string", project_year, "last_updated", "active")
    list_filter = ("active", "last_updated")
    search_fields = ("title", "description", "authors__first_name", "authors__last_name")
    actions = [mark_inactive]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Post)
admin.site.register(Photo)
