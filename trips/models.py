from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

SCORE = (
    (1, 'Very Dissatisfied'),
    (2, 'Dissatisfied'),
    (3, 'Neutral'),
    (4, 'Satisfied'),
    (5, 'Very Satisfied')
)


class Trip(models.Model):
    name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    destination = models.CharField(max_length=200)
    date_start = models.DateField(auto_now=False)
    date_end = models.DateField(auto_now=False)
    duration = models.IntegerField(default=0)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    price = models.IntegerField(default=0)
    registered_users = models.ManyToManyField(User, related_name='trip_registered_to', blank=True)

    class Meta:
        ordering = ['date_start']

    def __str__(self) -> str:
        return f'{self.name.capitalize()} at {self.destination.capitalize()}'

    def registered_users_count(self):
        return self.registered_users.count()


class Review(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    comment = models.TextField(blank=True)
    rating = models.IntegerField(choices=SCORE, default=3)
    submitted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_on']

    def __str__(self) -> str:
        return f'User {self.user} commented {self.comment} with a rating of {self.rating}'


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_request')
    destination = models.CharField(max_length=200)
    description = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['submitted_on']

    def __str__(self) -> str:
        return f'User {self.user} requested the destination {self.destination} with a description of {self.description}'
