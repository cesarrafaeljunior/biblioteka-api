# Generated by Django 4.1.7 on 2023-03-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_genders",
            field=models.ManyToManyField(
                default=None, related_name="books", to="books.gender"
            ),
        ),
    ]
