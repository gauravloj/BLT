# Generated by Django 4.2.7 on 2023-11-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0080_alter_issue_team_members"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="issue_downvoted",
            field=models.ManyToManyField(blank=True, related_name="downvoted", to="website.issue"),
        ),
    ]
