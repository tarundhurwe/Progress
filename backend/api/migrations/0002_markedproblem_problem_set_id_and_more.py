# Generated by Django 5.0.2 on 2024-03-29 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="markedproblem",
            name="problem_set_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.problemlist",
            ),
        ),
        migrations.AlterField(
            model_name="problemlist",
            name="problem_set_id",
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
