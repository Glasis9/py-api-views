from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        verbose_name_plural = "cinema_halls"

    def __str__(self):
        return f"{self.name} " \
               f"(rows: {self.rows}, seats in row: {self.seats_in_row})"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(
        Actor,
        related_name="movies"
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )
    duration = models.IntegerField()

    def __str__(self):
        return self.title
