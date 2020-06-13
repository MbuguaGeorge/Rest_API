from rest_framework import serializers
from django.contrib.auth.models import User
from iflix.models import Movie, User_Account

class MovieSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = ('url','pk', 'movie_name', 'thumbnail', 'video_id')
        read_only_fields = ['pk']

    def validate_movie_name(self, value):
        queryset = Movie.objects.filter(movie_name__iexact=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError("This Movie exists in our database")
        return value

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'date_joined', 'last_login')