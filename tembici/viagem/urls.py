from django.urls import path
from .views import LoginView, ListTripsView, TripUpdateView


urlpatterns = [
    path('trips/', ListTripsView.as_view(), name="trips-list"),
    path('trips_update/', TripUpdateView.as_view(), name="songs-update"),
    path('auth/login/', LoginView.as_view(), name="auth-login")
]