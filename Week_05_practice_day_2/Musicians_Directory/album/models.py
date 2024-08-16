from django.db import models
from musician.models import MusicianModel
from django.core.validators import MinValueValidator, MaxValueValidator

class AlbumModel(models.Model):
    Album_Name = models.CharField(max_length=100)
    Musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    Release_date = models.DateField()
    Rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f'{self.Album_Name} by {self.Musician.First_Name} {self.Musician.Last_Name}'

