from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .models import Trip, Category
from .serializers import TripsSerializer, CategoriesSerializer, TokenSerializer, UserSerializer

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    name = 'auth-login'
    """
    POST auth/login/
    """
    
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ListTripsView(generics.ListCreateAPIView):
    name = 'trips-list'
    """
    GET trips/
    """
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripsSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TripsSerializer(queryset, many=True)
        return Response(serializer.data)


class TripUpdateView(generics.UpdateAPIView):
    name = 'trip-update'
    """
    PUT trips/:id/
    """
    queryset = Trip.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            trip = self.queryset.get(pk=kwargs["pk"])
            serializer = TripsSerializer()
            updated_trip = serializer.update(trip, request.data)
            return Response(TripsSerializer(updated_trip).data)
        except Trip.DoesNotExist:
            return Response(
                data={
                    "message": "Trip with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


