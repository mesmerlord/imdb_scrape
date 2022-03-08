from django.contrib import admin
from .models import (Movie)

@admin.register(Movie)
class NovelAdmin(admin.ModelAdmin):
    list_display = ["title", "rank", "rating", "last_seen", "created_at"]
    search_fields = ['title']
