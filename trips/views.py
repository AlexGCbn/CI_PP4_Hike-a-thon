from django.shortcuts import render
from django.views import generic
from .models import Trip


class TripList(generic.ListView):
    model = Trip
    queryset = Trip.objects.order_by('date_start')
    template_name = 'index.html'
    paginate_by = 8
