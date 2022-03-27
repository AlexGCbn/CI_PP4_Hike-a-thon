from django.test import TestCase
from .models import Trip, User, Review, Request
import datetime


class TestViews(TestCase):

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
            description='Test description',
            image='default',
            price='50'
        )

        test_trip.registered_users.set([])

        User.objects.create_user(
            username='test_user',
            email='test_email@email.com',
            password='test_password'
        )

    def test_get_trip_list(self):
        """
        Test trip list GET
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_past_trips_list(self):
        """
        Test past trips GET
        """
        response = self.client.get('/past_trips/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'past_trips.html')

    def test_get_trip_detail(self):
        """
        Test trip detail GET
        """
        trip = Trip.objects.get(name='Test Trip')
        response = self.client.get(f'/{trip.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trip_detail.html')

    def test_post_trip_review(self):
        """
        Test trip review POST
        """
        user = self.client.login(
            username='test_user', password='test_password'
        )
        trip = Trip.objects.get(name='Test Trip')
        trip.registered_users.add(user)
        response = self.client.post(
            f'/{trip.slug}/', {'comment': 'This is a comment', 'rating': 3}
        )
        self.assertRedirects(response, f'/{trip.slug}/')

    def test_post_trip_review_bad(self):
        """
        Test trip review bad POST
        For invalid form data
        """
        self.client.login(username='test_user', password='test_password')
        user = User.objects.get(username='test_user')
        trip = Trip.objects.get(name='Test Trip')
        trip.registered_users.add(user)
        Review.objects.create(
            trip=trip, user=user, comment="Testing score", rating=5
        )
        response = self.client.post(
            f'/{trip.slug}/', {'comment': 'Test', 'rating': 3}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trip_detail.html')
        self.assertEqual(response.context['reviewed'], False)
        self.assertEqual(response.context['score'], 5)

    def test_trip_registration(self):
        """
        Test user trip registration
        """
        self.client.login(
            username='test_user', password='test_password'
        )
        trip = Trip.objects.get(name='Test Trip')
        response = self.client.post(f'/register/{trip.slug}')
        self.assertRedirects(response, f'/{trip.slug}/')
        response = self.client.post(f'/register/{trip.slug}')
        registered_users = trip.registered_users.all()
        self.assertQuerysetEqual(registered_users, [])

    def test_delete_review(self):
        """
        Test user review delete
        """
        user = self.client.login(
            username='test_user', password='test_password'
        )
        trip = Trip.objects.get(name='Test Trip')
        trip.registered_users.add(user)
        self.client.post(
            f'/{trip.slug}/', {'comment': 'This is a comment', 'rating': 3}
        )
        review = Review.objects.get(comment='This is a comment')
        self.assertEqual(review.comment, 'This is a comment')
        response = self.client.post(f'/delete_review/{trip.slug}')
        self.assertRedirects(response, f'/{trip.slug}/')
        new_review = Review.objects.all()
        self.assertEqual(len(new_review), 0)

    def test_dashboard(self):
        """
        Test user dashboard access
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_trip_request_get(self):
        """
        Test user past trip requests GET
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/dashboard/request/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'request.html')

    def test_trip_request_post(self):
        """
        Test user trip request POST
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.post(
            '/dashboard/request/',
            {'destination': 'Africa', 'description': 'Test description'}
        )
        self.assertRedirects(response, '/dashboard/request/')
        request = Request.objects.get(destination='Africa')
        self.assertEqual(request.destination, 'Africa')

    def test_trip_request_bad(self):
        """
        Test user bad trip request POST
        Provides invalid form data
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.post(
            '/dashboard/request/', {'destination': '', 'description': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'request.html')

    def test_edit_review(self):
        """
        Test user review edit
        """
        user = self.client.login(
            username='test_user', password='test_password'
        )
        trip = Trip.objects.get(name='Test Trip')
        trip.registered_users.add(user)
        self.client.post(
            f'/{trip.slug}/', {'comment': 'This is a comment', 'rating': 3}
        )
        review = Review.objects.get(comment='This is a comment')
        self.client.post(
            f'/edit/{review.id}',
            {'comment': 'This is a better comment', 'rating': 5}
        )
        review = Review.objects.get(comment='This is a better comment')
        self.assertEqual(review.comment, 'This is a better comment')
        self.assertEqual(review.rating, 5)
