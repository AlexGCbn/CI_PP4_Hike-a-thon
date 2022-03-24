from django.test import TestCase
from .forms import ReviewForm, RequestForm


class TestReviewForm(TestCase):

    def test_comment_is_required(self):
        form = ReviewForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')

    def test_comment_validation(self):
        form = ReviewForm({'comment': 'Hi'})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'Please input more than 5 characters.')

    def test_rating_is_required(self):
        form = ReviewForm({'comment': 'This is a comment', 'rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_fields_are_explicit(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ('comment', 'rating'))
