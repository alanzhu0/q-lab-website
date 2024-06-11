from django.contrib import admin

from .models import CarouselPhoto, ResearchPartner, Resource, Song, User, College


@admin.action(description="Mark as Lab Student")
def mark_lab_student(modeladmin, request, queryset):
    queryset.update(is_lab_student=True)
    queryset.update(is_alumni=False)

@admin.action(description="Mark as Alumni")
def mark_alumni(modeladmin, request, queryset):
    queryset.update(is_lab_student=False)
    queryset.update(is_alumni=True)

@admin.action(description="Display First/Last Name")
def display_first_last(modeladmin, request, queryset):
    queryset.update(display_first_last=True)

def full_name(obj):
    return f"{obj.first_name} {obj.last_name}"

class UserAdmin(admin.ModelAdmin):
    actions = [mark_lab_student, mark_alumni, display_first_last]
    list_display = (full_name, "graduation_year", "is_lab_student", "is_alumni", "display_first_last")


admin.site.register(CarouselPhoto)
admin.site.register(ResearchPartner)
admin.site.register(Resource)
admin.site.register(Song)
admin.site.register(User, UserAdmin)
admin.site.register(College)
