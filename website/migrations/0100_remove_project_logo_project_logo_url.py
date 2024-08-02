# Generated by Django 5.0.7 on 2024-08-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0099_winner_prize_winner_prize_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="logo",
        ),
        migrations.AddField(
            model_name="project",
            name="logo_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
    ]