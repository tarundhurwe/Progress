# Generated by Django 5.0.2 on 2024-04-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_problem_problem_difficulty_problem_problem_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problem",
            name="problem_type",
            field=models.CharField(default="", max_length=250),
        ),
    ]
