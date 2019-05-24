from django.db import models
from django.utils.timezone import now

class Twice(models.Model):
    CHOICE = (
        ('한국', 'KR'),
        ('일본', 'JP'),
        ('대만', 'TW')
    )
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    birth = models.DateField(default = now)
    nationality = models.CharField(max_length = 20,
        choices = CHOICE)
    position = models.TextField(max_length=20)
    def __str__(self):
        return self.name