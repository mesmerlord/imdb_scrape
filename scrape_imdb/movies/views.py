from rest_framework.decorators import api_view
from rest_framework.response import Response
from scrape_imdb.movies.models import Movie
from scrape_imdb.movies.serializers import MovieSearchSerializer
from .tasks import scrape_imdb
from rest_framework import viewsets, filters, pagination

@api_view(['GET', 'POST'])
def scrape_movies(request):
    if request.user.is_staff:
        scrape_imdb.delay()
        return Response({"message": 'Scraping in progress. Visit http://127.0.0.1:5555/tasks for the status of the task. For local development the username is "test" and password is "test"'})
    return Response({"message": "You're not authorized for this"})

class SearchPagination(pagination.PageNumberPagination):       
    page_size = 20

class MovieSerializerView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    pagination_class = SearchPagination
    serializer_class = MovieSearchSerializer
    search_fields = ['title']
    filter_backends = [filters.SearchFilter]
