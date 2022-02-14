from . import views
from django.urls import path

urlpatterns = [
    path('', views.TripList.as_view(), name='home')  # Home URL
]
