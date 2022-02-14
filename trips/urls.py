from . import views
from django.urls import path

urlpatterns = [
    path('', views.TripList.as_view(), name='home'),  # Home URL
    path('<slug:slug>/', views.TripDetail.as_view(), name='trip_detail'),  # Trip detail URL
]
