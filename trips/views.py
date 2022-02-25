from pdb import post_mortem
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Review, Trip
from .forms import ReviewForm


class TripList(generic.ListView):
    """
    Main trips view
    """
    model = Trip
    queryset = Trip.objects.order_by('date_start')
    template_name = 'index.html'
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
        for review in reviews:
            score = score + review.rating
            index += 1
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
                'reviewed': False,
                'score': score,
                'registered': registered,
                'review_form': ReviewForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Trip.objects
        trip = get_object_or_404(queryset, slug=slug)
        reviews = trip.reviews.order_by('-submitted_on')
        score = 0
        index = 0
        for review in reviews:
            score = score + review.rating
            index += 1
        if score != 0:
            score = score / index

        registered = False
        if trip.registered_users.filter(id=request.user.id).exists():
            registered = True

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.trip = trip
            review.user = request.user
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            'trip_detail.html',
            {
                'trip': trip,
                'reviews': reviews,
                'reviewed': True,
                'score': score,
                'registered': registered,
                'review_form': ReviewForm()
            }
        )


class TripRegistration(View):

    def post(self, request, slug, *args, **kwargs):
        trip = get_object_or_404(Trip, slug=slug)
        if trip.registered_users.filter(id=request.user.id).exists():
            trip.registered_users.remove(request.user)
        else:
            trip.registered_users.add(request.user)

        return HttpResponseRedirect(reverse('trip_detail', args=[slug]))
