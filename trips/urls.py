from . import views
from django.urls import path

urlpatterns = [
    path('', views.TripList.as_view(), name='home'),  # Home URL
    path('dashboard/', views.TripsRegistered.as_view(), name='user_dashboard'),  # Trips history / user dashboard URL
    path('dashboard/request/', views.TripRequest.as_view(), name='trip_request'),  # Trip reqeust URL
    path('past_trips/', views.PastTrips.as_view(), name='past_trips'),  # Past trips URL
    path('<slug:slug>/', views.TripDetail.as_view(), name='trip_detail'),  # Trip detail URL
    path('register/<slug:slug>', views.TripRegistration.as_view(), name='trip_registration'),  # Trip registration URL
    path('delete_review/<slug:slug>', views.DeleteReview.as_view(), name='delete_review'),  # Trip registration URL
    path('edit/<pk>', views.EditReview.as_view(), name='edit_review'),  # Edit review URL
]
