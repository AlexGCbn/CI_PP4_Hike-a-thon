from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Trip


class TripList(generic.ListView):
    """
    Main trips view
    """
    model = Trip
    queryset = Trip.objects.order_by('date_start')
    template_name = 'index.html'
    paginate_by = 8


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

        return render(
            request,
            'trip_detail.html',
            {
                'trip': trip,
                'reviews': reviews,
                'score': score
            }
        )
