# Generated by Django 4.1.7 on 2023-03-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_is_blocked_user_is_collaborator"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="unlock_date",
            field=models.DateField(default=None),
        ),
    ]
