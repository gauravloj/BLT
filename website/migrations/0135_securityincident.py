# Generated by Django 5.0.8 on 2024-08-22 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0134_blocked_modified"),
    ]

    operations = [
        migrations.CreateModel(
            name="SecurityIncident",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "severity_level",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Low"),
                            (1, "Medium"),
                            (2, "High"),
                            (3, "Critical"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "incident_status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Open"), (1, "In Progress"), (2, "Closed")],
                        default=0,
                    ),
                ),
                ("description", models.TextField()),
                ("title", models.CharField(default="", max_length=200)),
                ("occurance_date", models.DateField(auto_now_add=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="website.company",
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="website.tag")),
            ],
        ),
    ]