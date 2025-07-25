from django.db import models
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas')
        ]
    )
    comment = models.TextField(max_length=500, null=True, blank=True)
