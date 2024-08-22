from django.db import models
from datetime import date


class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class Movie(models.Model):
    year_now = date.today().year

    title = models.CharField(max_length=50)
    year = models.IntegerField(
        choices=[(x, x) for x in range(1911, year_now + 1)],
        default=year_now
    )
    description = models.TextField(blank=True)
    actors = models.CharField(max_length=200, blank=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"
    
    class Meta:
        ordering = ['title']

    
class Review(models.Model):
    email = models.EmailField()
    stars = models.IntegerField(
        choices=[(x, x) for x in range(0, 11)],
        default=0,
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.email}, {self.movie} : {self.stars}"
    
    class Meta:
        ordering = ['-time']
