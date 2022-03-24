from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.TripList.as_view(), name='home'),  # Home URL
    path('dashboard/', login_required(views.TripsRegistered.as_view()), name='user_dashboard'),  # Trips history / user dashboard URL
    path('dashboard/request/', login_required(views.TripRequest.as_view()), name='trip_request'),  # Trip reqeust URL
    path('past_trips/', views.PastTrips.as_view(), name='past_trips'),  # Past trips URL
    path('<slug:slug>/', views.TripDetail.as_view(), name='trip_detail'),  # Trip detail URL
    path('register/<slug:slug>', login_required(views.TripRegistration.as_view()), name='trip_registration'),  # Trip registration URL
    path('delete_review/<slug:slug>', login_required(views.DeleteReview.as_view()), name='delete_review'),  # Trip registration URL
    path('edit/<pk>', login_required(views.EditReview.as_view()), name='edit_review'),  # Edit review URL
]
