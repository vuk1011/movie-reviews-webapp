from django.contrib import admin
from .models import Genre, Movie, Review


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'actors', 'joined_genres')

    @admin.display(description="Genres")
    def joined_genres(self, obj):
        strings = [str(g) for g in obj.genres.all()]
        return ", ".join(strings)
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('email', 'stars', 'movie', 'time')

# Register your models here.

admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
