from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'genres', views.GenreView, 'genre')
router.register(r'movies', views.MovieView, 'movie')
router.register(r'reviews', views.ReviewView, 'review')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]
