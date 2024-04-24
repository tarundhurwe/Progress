from django.contrib import admin
from .models import ProblemList, Problem, Note


# Register your models here.
admin.site.register(ProblemList)
admin.site.register(Problem)
admin.site.register(Note)
