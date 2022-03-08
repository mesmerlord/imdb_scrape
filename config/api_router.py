from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from scrape_imdb.movies.views import  MovieSerializerView, scrape_movies

from scrape_imdb.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("movies", MovieSerializerView)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("utils/scrape_movies" , scrape_movies)
]
