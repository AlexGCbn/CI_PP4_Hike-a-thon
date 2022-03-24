from django.test import TestCase
from .models import Trip, User, Review
from .forms import ReviewForm
import datetime


class TestViews(TestCase):

    def setUp(self):
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

        User.objects.create_user(username='test_user', email='test_email@email.com', password='test_password')

    def test_get_trip_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_past_trips_list(self):
        response = self.client.get('/past_trips/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'past_trips.html')

    def test_get_trip_detail(self):
        trip = Trip.objects.get(name='Test Trip')
        response = self.client.get(f'/{trip.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trip_detail.html')

    def test_post_trip_review(self):
        user = self.client.login(username='test_user', password='test_password')
        trip = Trip.objects.get(name='Test Trip')
        trip.registered_users.add(user)
        response = self.client.post(f'/{trip.slug}/', {'comment': 'This is a comment', 'rating': 3})
        self.assertRedirects(response, f'/{trip.slug}/')

    def test_trip_registration(self):
        self.client.login(username='test_user', password='test_password')
        trip = Trip.objects.get(name='Test Trip')
        response = self.client.post(f'/register/{trip.slug}')
        self.assertRedirects(response, f'/{trip.slug}/')

    def test_delete_review(self):
        user = self.client.login(username='test_user', password='test_password')
        trip = Trip.objects.get(name='Test Trip')
        trip.registered_users.add(user)
        self.client.post(f'/{trip.slug}/', {'comment': 'This is a comment', 'rating': 3})
        review = Review.objects.get(comment='This is a comment')
        self.assertEqual(review.comment, 'This is a comment')
        response = self.client.post(f'/delete_review/{trip.slug}')
        self.assertRedirects(response, f'/{trip.slug}/')
        new_review = Review.objects.all()
        self.assertEqual(len(new_review), 0)
        

    # def test_registered_trips(self):


    # def test_trip_request_get(self):


    # def test_trip_request_post(self):


    # def test_edit_review(self):
