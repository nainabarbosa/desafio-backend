from django.urls import path
from .views import LoginView, ListTripsView, TripUpdateView


urlpatterns = [
    path('trips/$', ListTripsView.as_view(), name=ListTripsView.name),
    path('trip_update/(?P<pk>[0-9]+)/$', TripUpdateView.as_view(), name=TripUpdateView.name),
    path('auth/login/$', LoginView.as_view(), name=LoginView.name)
]