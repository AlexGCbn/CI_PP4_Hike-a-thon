from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime

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

    def is_completed(self):
        if self.date_start <= datetime.date.today():
            return True
        else:
            return False


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

    def get_range(self) -> list:
        """
        Returns list (range) of the rating, used to display stars.
        Credits: https://stackoverflow.com/questions/2969649/how-to-loop-x-times-in-django
        """
        return range(self.rating)


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_request')
    destination = models.CharField(max_length=200)
    description = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['submitted_on']

    def __str__(self) -> str:
        return f'User {self.user} requested the destination {self.destination} with a description of {self.description}'


class ContactThread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_message_thread')
    name = models.CharField(max_length=500, unique=True, null=True)
    slug = models.SlugField(max_length=500, unique=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self) -> str:
        return f'User {self.user} has sent messages to admin.'


class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_message')
    thread = models.ForeignKey(ContactThread, on_delete=models.CASCADE, related_name='thread_message')
    message = models.CharField(max_length=1000, blank=False, null=False)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_on']

    def __str__(self) -> str:
        return f'User {self.user} messaged the following: {self.message}'
