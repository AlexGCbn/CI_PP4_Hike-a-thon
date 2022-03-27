from django.test import TestCase
from .models import Trip, User, Review, Request
import datetime


class TestModels(TestCase):

    def setUp(self):
        """
        setUp function
        Creates a trip object
        Creates a user object
        """
        test_trip = Trip.objects.create(
            name='Test Trip',
            slug='test_trip',
            destination='Test Destination',
            date_start=datetime.date.today(),
            date_end=datetime.date.today(),
            description='Test description'
        )
        test_trip.registered_users.set([])
        User.objects.create_user(
            username='test_user',
            email='test_email@email.com',
            password='test_password'
        )

    def test_trip_defaults(self):
        """
        Test Trip default values
        """
        trip = Trip.objects.get(name='Test Trip')
        # Unable to test default image
        self.assertEqual(trip.price, 0)

    def test_review_default(self):
        """
        Test Review default values
        """
        self.client.login(
            username='test_user', password='test_password'
        )
        user = User.objects.get(username='test_user')
        trip = Trip.objects.get(name='Test Trip')
        trip.registered_users.add(user)
        review = Review.objects.create(
            trip=trip, user=user, comment='This is a comment'
        )
        self.assertEqual(review.rating, 3)

    def test_trip_str(self):
        """
        Test Trip __str__ function
        """
        trip = Trip.objects.get(name='Test Trip')
        self.assertEqual(
            trip.__str__(), 'Test trip at Test destination'
        )

    def test_trip_is_completed(self):
        """
        Test Trip is_completed function
        """
        tomorrow_trip = Trip.objects.create(
            name='Test tomorrow Trip',
            slug='test_tomorrow_trip',
            destination='Test Destination',
            date_start=datetime.date(2023, 1, 1),
            date_end=datetime.date(2023, 1, 1),
            description='Test description'
        )
        self.assertEqual(tomorrow_trip.is_completed(), False)

    def test_review_str(self):
        """
        Test Review __str__ function
        """
        self.client.login(
            username='test_user', password='test_password'
        )
        user = User.objects.get(username='test_user')
        trip = Trip.objects.get(name='Test Trip')
        trip.registered_users.add(user)
        review = Review.objects.create(
            trip=trip, user=user, comment='This is a comment'
        )
        self.assertEqual(
            review.__str__(),
            f'User {user.username} commented '
            f'{review.comment} with a rating of {review.rating}'
        )

    def test_Request_str(self):
        """
        Test Request __str__ function
        """
        self.client.login(
            username='test_user', password='test_password'
        )
        user = User.objects.get(username='test_user')
        response = self.client.post(
            '/dashboard/request/',
            {'destination': 'Africa', 'description': 'Test description'}
        )
        self.assertRedirects(response, '/dashboard/request/')
        request = Request.objects.get(destination='Africa')
        self.assertEqual(
            request.__str__(), f'User {user.username} '
            f'requested the destination {request.destination} '
            f'with a description of {request.description}'
        )
