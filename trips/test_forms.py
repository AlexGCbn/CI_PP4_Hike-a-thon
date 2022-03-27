from django.test import TestCase
from .forms import ReviewForm, RequestForm


class TestReviewForm(TestCase):

    def test_comment_is_required(self):
        form = ReviewForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(
            form.errors['comment'][0], 'This field is required.'
        )

    def test_comment_validation(self):
        form = ReviewForm({'comment': 'Hi'})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(
            form.errors['comment'][0],
            'Please input more than 5 characters.'
        )

    def test_rating_is_required(self):
        form = ReviewForm(
            {'comment': 'This is a comment', 'rating': ''}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(
            form.errors['rating'][0],
            'This field is required.'
            )

    def test_fields_are_explicit(self):
        form = ReviewForm()
        self.assertEqual(
            form.Meta.fields, ('comment', 'rating')
        )


class TestRequestForm(TestCase):

    def test_destination_is_required(self):
        form = RequestForm({'destination': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('destination', form.errors.keys())
        self.assertEqual(
            form.errors['destination'][0], 'This field is required.'
        )

    def test_destination_validation(self):
        form = RequestForm({'destination': 'Hi'})
        self.assertFalse(form.is_valid())
        self.assertIn('destination', form.errors.keys())
        self.assertEqual(
            form.errors['destination'][0],
            'Please input more than 5 characters.'
        )

    def test_description_is_required(self):
        form = RequestForm(
            {'destination': 'This is a destination', 'description': ''}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.'
        )

    def test_description_validation(self):
        form = RequestForm(
            {'destination': 'This is a destination', 'description': 'Hi'}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0],
            'Please input more than 5 characters.'
        )

    def test_fields_are_explicit(self):
        form = RequestForm()
        self.assertEqual(form.Meta.fields, ('destination', 'description'))
