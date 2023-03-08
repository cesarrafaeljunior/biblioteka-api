from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Copy(models.Model):
    ammounts_of_copies = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    copies_avaliable = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
