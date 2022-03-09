from . import views
from django.urls import path

urlpatterns = [
    path('', views.TripList.as_view(), name='home'),  # Home URL
    path('dashboard/', views.TripsRegistered.as_view(), name='user_dashboard'),  # Trips history / user dashboard URL
    path('<slug:slug>/', views.TripDetail.as_view(), name='trip_detail'),  # Trip detail URL
    path('register/<slug:slug>', views.TripRegistration.as_view(), name='trip_registration'),  # Trip registration URL
]
