from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("actors",views.ActorViewSet,basename="actors")

router.register("albums",views.AlbumViewSetView,basename="albums")

router.register("tracks",views.TrackViewSetView,basename="tracks")

urlpatterns=[
    path("movies/",views.MovieListCreateView.as_view()),
    path('movies/<int:pk>/',views.MovieRetriveUpdateDestroyView.as_view()),

    path("movies/languages/",views.LanguageView.as_view()),

    path("movies/genres/",views.GenreView.as_view())

]+router.urls