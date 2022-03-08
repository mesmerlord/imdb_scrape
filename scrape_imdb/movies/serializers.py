from .models import Movie
from rest_framework import serializers


class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
