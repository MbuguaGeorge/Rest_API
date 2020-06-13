from rest_framework import serializers, generics
from rest_framework.views import APIView
from api.serializers import MovieSerializer, UserSerializer
from iflix.models import Movie
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token

class movielist(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Movie.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class moviecreation(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class userlist(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()

class usercreation(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.all()

class TokenView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
