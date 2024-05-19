from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProblemList(models.Model):
    problem_set_id = models.AutoField(primary_key=True, default=0)
    problem_set_name = models.CharField(max_length=250, blank=False)
    author = models.CharField(max_length=250)
    link = models.URLField(max_length=250, blank=True, unique=True)

    def __str__(self) -> str:
        return f"{self.problem_set_name}"


class Problem(models.Model):
    difficulty_choice = (("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard"))
    problem_id = models.AutoField(primary_key=True)
    problem_set_id = models.ForeignKey(ProblemList, on_delete=models.CASCADE)
    problem_name = models.CharField(max_length=250, blank=False)
    problem_type = models.CharField(max_length=250, blank=False, default="")
    problem_difficulty = models.CharField(
        max_length=20, choices=difficulty_choice, default="Easy"
    )
    problem_link = models.URLField(max_length=250, blank=False)

    def __str__(self) -> str:
        return f"{self.problem_name}"


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self) -> str:
        return f"{self.title}"


class Status(models.Model):
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    problem_set_id = models.ForeignKey(
        ProblemList, on_delete=models.CASCADE, default=None
    )
    status = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.problem_id}"

    class Meta:
        verbose_name_plural = "Status"
