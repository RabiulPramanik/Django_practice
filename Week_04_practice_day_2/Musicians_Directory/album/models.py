from django.db import models
from musician.models import MusicianModel
from django.core.validators import MinValueValidator, MaxValueValidator

class AlbumModel(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self) -> str:
        return f'{self.name} by {self.musician.first_name} {self.musician.last_name}'
