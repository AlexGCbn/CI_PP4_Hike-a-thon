from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .validators import validate_comment
import datetime

# Score variable, used to provide choice of rating.
SCORE = (
    (1, 'Very Dissatisfied'),
    (2, 'Dissatisfied'),
    (3, 'Neutral'),
    (4, 'Satisfied'),
    (5, 'Very Satisfied')
)


class Trip(models.Model):
    """
    Trip class based model
    """
    name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    destination = models.CharField(max_length=200)
    date_start = models.DateField(auto_now=False)
    date_end = models.DateField(auto_now=False)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    price = models.IntegerField(default=0)
    registered_users = models.ManyToManyField(
        User, related_name='trip_registered_to', blank=True
    )

    class Meta:
        ordering = ['date_start']

    def __str__(self) -> str:
        return f'{self.name.capitalize()} at {self.destination.capitalize()}'

    def registered_users_count(self) -> int:
        """
        Returns count of registered users
        """
        return self.registered_users.count()

    def is_completed(self) -> bool:
        """
        Returns boolean value if trip is completed
        """
        if self.date_start <= datetime.date.today():
            return True
        else:
            return False


class Review(models.Model):
    """
    Review class based model
    """
    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_reviews'
    )
    comment = models.TextField(blank=False, validators=[validate_comment])
    rating = models.IntegerField(choices=SCORE, default=3)
    submitted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_on']

    def __str__(self) -> str:
        return (
            f'User {self.user} commented {self.comment} '
            f'with a rating of {self.rating}'
        )

    def get_range(self) -> list:
        """
        Returns list (range) of the rating, used to display stars.
        Credits:
        https://stackoverflow.com/questions/2969649/how-to-loop-x-times-in-django
        """
        return range(self.rating)


class Request(models.Model):
    """
    Request class based model
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_request'
    )
    destination = models.CharField(
        max_length=50, validators=[validate_comment]
    )
    description = models.TextField(
        max_length=200, validators=[validate_comment]
    )
    submitted_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['submitted_on']

    def __str__(self) -> str:
        return (
            f'User {self.user} requested the destination '
            f'{self.destination} with a description of {self.description}'
        )
