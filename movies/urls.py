from django.urls import path

from . import views


urlpatterns = [

    path('movies/', views.MovieListView.as_view(), name="movies_create_list"),
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyView.as_view(), name="movies_detail_view"),
    path('movies/stats/', views.MovieStatsView.as_view(), name="movies_stats_view"),
]
