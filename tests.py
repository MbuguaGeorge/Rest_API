from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from iflix.models import Movie

User = get_user_model()

class MovielistApiTest(APITestCase):
    def setUp(self):
        user = User(username='Martin', email='njoro@gmail.com')
        user.set_password=('njoroge026#')
        user.save()

        movies = Movie.objects.create(
            movie_name = 'grownish',
            thumbnail = 'http://127.0.0.1:8000/media/belgravia.jpg',
            video_id = 5
        )
    
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_movie(self):
        movie_count = Movie.objects.count()
        self.assertEqual(movie_count, 1)

    def test_get_list(self):
        data={}
        url = api_reverse("iflix_api:review")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
