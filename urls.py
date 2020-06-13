from django.urls import path
from api.views import movielist, moviecreation, userlist, usercreation, TokenView
from api import views


app_name = 'iflix_api'
urlpatterns = [
    path('movies/<int:pk>/', views.movielist.as_view(), name='movie_s'),
    path('movies/', views.moviecreation.as_view(), name='review'),
    path('users/', views.userlist.as_view()),
    path('users/<int:pk>/', views.usercreation.as_view(), name='user_s'),
    path('token/', views.TokenView.as_view()),
]