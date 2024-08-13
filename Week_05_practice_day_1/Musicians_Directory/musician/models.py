from django.db import models

class MusicianModel(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=11)
    Instrument_Type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.First_Name} {self.Last_Name}'

