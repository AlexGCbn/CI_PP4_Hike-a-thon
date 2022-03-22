from xml.dom import ValidationErr
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, get_list_or_404
from django.views import generic, View
from .models import Review, Trip, Request
from .forms import ReviewForm, RequestForm


class TripList(generic.ListView):
    """
    Main trips view
    """
    model = Trip
    queryset = Trip.objects.order_by('date_start')
    template_name = 'index.html'
    paginate_by = 3


class PastTrips(generic.ListView):
    """
    Past trips view
    """
    model = Trip
    queryset = Trip.objects.order_by('date_start')
    template_name = 'past_trips.html'
    paginate_by = 3

class TripDetail(View):
    """
    Trip detail view, to render each trip
    """

    def get(self, request, slug, *args, **kwargs):
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

        return render(
            request,
            'trip_detail.html',
            {
                'trip': trip,
                'reviews': reviews,
                'reviewed': reviewed,
                'score': score,
                'registered': registered,
                'review_form': ReviewForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Trip.objects
        trip = get_object_or_404(queryset, slug=slug)
        reviews = trip.reviews.order_by('-submitted_on')
        # score = 0
        # index = 0
        reviewed = False
        for review in reviews:
            # score = score + review.rating
            # index += 1
            if review.user == request.user:
                reviewed = True
        # if score != 0:
        #     score = score / index

        # registered = False
        # if trip.registered_users.filter(id=request.user.id).exists():
        #     registered = True

        review_form = ReviewForm(data=request.POST)
        if (not reviewed):
            if review_form.is_valid():
                review_form.instance.email = request.user.email
                review_form.instance.name = request.user.username
                review = review_form.save(commit=False)
                review.trip = trip
                review.user = request.user
                review.save()
            else:
                review_form = ReviewForm()

        return HttpResponseRedirect(reverse('trip_detail', args=[slug]))

        # return render(
        #     request,
        #     'trip_detail.html',
        #     {
        #         'trip': trip,
        #         'reviews': reviews,
        #         'reviewed': reviewed,
        #         'score': score,
        #         'registered': registered,
        #         'review_form': ReviewForm()
        #     }
        # )


class TripRegistration(View):

    def post(self, request, slug, *args, **kwargs):
        trip = get_object_or_404(Trip, slug=slug)
        if trip.registered_users.filter(id=request.user.id).exists():
            trip.registered_users.remove(request.user)
        else:
            trip.registered_users.add(request.user)

        return HttpResponseRedirect(reverse('trip_detail', args=[slug]))


class DeleteReview(View):

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
        trips = Trip.objects.order_by('-date_start').filter(registered_users=request.user)

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
    Also GET user's requests
    """

    def get(self, request, *args, **kwargs):
        requests = Request.objects.filter(user=request.user)

        return render(
            request,
            'request.html',
            {
                'requests': requests,
                'request_form': RequestForm()
            }
        )

    def post(self, request, *args, **kwargs):
        requests = Request.objects.filter(user=request.user)

        request_form = RequestForm(data=request.POST)

        if request_form.is_valid():
            # destination = request_form.cleaned_data['destination']
            # if not Request.objects.filter(destination=destination).exists():
            trip_request = request_form.save(commit=False)
            trip_request.user = request.user
            trip_request.save()

        return render(
            request,
            'request.html',
            {
                'requests': requests,
                'request_form': RequestForm()
            }
        )
