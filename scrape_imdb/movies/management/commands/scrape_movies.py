from django.core.management.base import BaseCommand, CommandError
from scrape_imdb.movies.tasks import scrape_function

class Command(BaseCommand):
    help = 'Scrape movies from IMDB and update model in database'

    def handle(self, *args, **options):
        
        created_movies , updated_movies = scrape_function()
        self.stdout.write(self.style.SUCCESS(f"Movie Scrape done. {created_movies} movies created, {updated_movies} movies updated."))