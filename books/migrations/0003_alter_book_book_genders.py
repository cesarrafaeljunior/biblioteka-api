# Generated by Django 4.1.7 on 2023-03-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_alter_book_book_genders"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_genders",
            field=models.ManyToManyField(related_name="books", to="books.gender"),
        ),
    ]