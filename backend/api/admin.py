from django.contrib import admin
from .models import ProblemList, Problem, Note, Status


# Register your models here.
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["problem_id", "problem_set_id", "status", "user_id"]


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = [
        "problem_set_id",
        "problem_name",
        "problem_type",
        "problem_difficulty",
    ]


@admin.register(ProblemList)
class ProblemListAdmin(admin.ModelAdmin):
    list_display = ["problem_set_name", "author", "link"]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "updated_at", "problem_id", "author"]
