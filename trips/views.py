from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Review, Trip, Request
from .forms import ReviewForm, RequestForm
from django import forms
import datetime


class TripList(generic.ListView):
    """
    Main trips view
    """
    model = Trip
    queryset = Trip.objects.order_by('date_start').filter(
        date_start__gt=datetime.date.today()
    )
    template_name = 'index.html'
    paginate_by = 3


class PastTrips(generic.ListView):
    """
    Past trips view
    """
    model = Trip
    queryset = Trip.objects.order_by('date_start').filter(
        date_start__lte=datetime.date.today()
    )
    template_name = 'past_trips.html'
    paginate_by = 3


class TripDetail(View):
    """
    Trip detail view, to render the trip on its own
    """
    def get(self, request, slug, *args, **kwargs):
        """
        GET request for TripDetail
        Returns the render of the trip detail
        """
        queryset = Trip.objects
        trip = get_object_or_404(queryset, slug=slug)
        reviews = trip.reviews.order_by('-submitted_on')
        score = 0
        index = 0
        reviewed = False
        for review in reviews:
            score = score + review.rating
            index += 1
            if review.user == request.user:
                reviewed = True
        if score != 0:
            score = score / index

        registered = False
        if trip.registered_users.filter(id=request.user.id).exists():
            registered = True

        review_form = ReviewForm()

        return render(
            request,
            'trip_detail.html',
            {
                'trip': trip,
                'reviews': reviews,
                'reviewed': reviewed,
                'score': score,
                'registered': registered,
                'review_form': review_form
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        POST request for TripDetail, to post reviews
        If review form is valid, makes POST and redirects
        If not, renders the TripDetail, as GET
        """
        queryset = Trip.objects
        trip = get_object_or_404(queryset, slug=slug)
        reviews = trip.reviews.order_by('-submitted_on')
        score = 0
        index = 0
        reviewed = False
        for review in reviews:
            score = score + review.rating
            index += 1
        if score != 0:
            score = score / index

        if trip.registered_users.filter(id=request.user.id).exists():
            registered = True

        review_form = ReviewForm(data=request.POST)
        if (not reviewed):
            if review_form.is_valid():
                review_form.instance.email = request.user.email
                review_form.instance.name = request.user.username
                review = review_form.save(commit=False)
                review.trip = trip
                review.user = request.user
                review.save()
                return HttpResponseRedirect(
                    reverse('trip_detail', args=[slug])
                )
            else:
                return render(
                    request,
                    'trip_detail.html',
                    {
                        'trip': trip,
                        'reviews': reviews,
                        'reviewed': reviewed,
                        'score': score,
                        'registered': registered,
                        'review_form': review_form
                    }
                )


class TripRegistration(View):
    """
    Trip Registration view, to POST user registration to trip
    """
    def post(self, request, slug, *args, **kwargs):
        trip = get_object_or_404(Trip, slug=slug)
        if trip.registered_users.filter(id=request.user.id).exists():
            trip.registered_users.remove(request.user)
        else:
            trip.registered_users.add(request.user)

        return HttpResponseRedirect(reverse('trip_detail', args=[slug]))


class DeleteReview(View):
    """
    Delete Review POST view, to delete user review
    """
    def post(self, request, slug, *args, **kwargs):
        trip = get_object_or_404(Trip, slug=slug)
        review = trip.reviews.filter(user=request.user)
        review.delete()

        return HttpResponseRedirect(reverse('trip_detail', args=[slug]))


class TripsRegistered(generic.TemplateView):
    """
    List view to show all user registered trips
    """
    def get(self, request, *args, **kwargs):
        trips = Trip.objects.order_by('-date_start').filter(
            registered_users=request.user
        )

        return render(
            request,
            'dashboard.html',
            {
                'trips': trips,
            }
        )


class TripRequest(View):
    """
    Display form for user to make a trip request
    """

    def get(self, request, *args, **kwargs):
        """
        GET request, to get user's past trip requests
        Gets only 5 results
        """
        requests = Request.objects.order_by('-submitted_on').filter(
            user=request.user
        )[:5]

        return render(
            request,
            'request.html',
            {
                'requests': requests,
                'request_form': RequestForm()
            }
        )

    def post(self, request, *args, **kwargs):
        """
        POST request, to send user's trip request
        If form is valid, it makes the POST
        If not, it renders the page again
        """
        requests = Request.objects.order_by('-submitted_on').filter(
            user=request.user
        )[:5]

        request_form = RequestForm(data=request.POST)

        if request_form.is_valid():
            trip_request = request_form.save(commit=False)
            trip_request.user = request.user
            trip_request.save()
            return HttpResponseRedirect(reverse('trip_request'))
        else:
            return render(
                request,
                'request.html',
                {
                    'requests': requests,
                    'request_form': RequestForm()
                }
            )


class EditReview(generic.UpdateView):
    """
    Allows user to edit their review
    """
    model = Review
    fields = ['comment', 'rating']
    template_name = 'edit_review_form.html'

    def get_success_url(self) -> str:
        """
        Returns url to use if edit is successful
        """

        slug = self.object.trip.slug
        return reverse('trip_detail', args=[slug])
