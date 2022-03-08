from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Movie(BaseModel):
    title = models.CharField(_("Name of Movie"), max_length=255, unique=True)
    rank = models.IntegerField(_("Rank of Movie"))
    link = models.TextField(_("Link of IMDB page"))
    rating = models.DecimalField(
        _("IMDB Rating"), blank=True, default=0.0, max_digits=3, decimal_places=2
    )
    last_seen = models.DateTimeField(_("Movie Last Seen At"), default=now)
    first_seen = models.DateTimeField(_("Movie First Seen At"), default=now)

    class Meta:
        ordering = ["rank"]
