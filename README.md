# scrape_imdb

## Basic Commands

- To start all containers, use this command:
  $ docker-compose -f local.yml up
- To rebuild containers, use this command:
  $ docker-compose -f local.yml up --build
- To deploy on a server containers, first create all the necessary env files with correct variables at .envs/.production/ the use command:
  $ docker-compose -f production.yml up

## Run Scrape

You can run the scrape command two ways, one asynchronous one not:

- First way is by using the management command, to use it in docker use
  $ docker-compose -f local.yml run django python manage.py scrape_movies
- Second, you can use go to "http://127.0.0.1:8000/api/utils/scrape_movies" which will trigger the scrape using celery and you'll receive task info there.

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

### Setting Up Your Users

- To create an **superuser account**, use this command:

      $ docker-compose -f local.yml run django python manage.py createsuperuser

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd scrape_imdb
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
