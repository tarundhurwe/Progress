# Generated by Django 5.0.2 on 2024-04-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_problem_problem_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problem",
            name="problem_difficulty",
            field=models.CharField(
                choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")],
                default="Easy",
                max_length=20,
            ),
        ),
    ]
