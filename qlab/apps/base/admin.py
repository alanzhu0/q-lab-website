from django.contrib import admin

from .models import ResearchPartner, Song, User


@admin.action(description="Mark as Lab Student")
def mark_lab_student(modeladmin, request, queryset):
    queryset.update(is_lab_student=True)
    queryset.update(is_alumni=False)

@admin.action(description="Mark as Alumni")
def mark_alumni(modeladmin, request, queryset):
    queryset.update(is_lab_student=False)
    queryset.update(is_alumni=True)


class UserAdmin(admin.ModelAdmin):
    actions = [mark_lab_student, mark_alumni]


admin.site.register(ResearchPartner)
admin.site.register(Song)
admin.site.register(User, UserAdmin)
