from django.db.models import Count, Avg

from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieStatsSerializer, MovieListDetailSerializer
from reviews.models import Review


class MovieListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        total_reiews = Review.objects.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        avarege_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        data = {
            'total_movies': total_movies,
            'total_reviews': total_reiews,
            'movies_by_genre': list(movies_by_genre),
            'average_stars': round(avarege_stars, 1) if avarege_stars else 0,
        }
        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK,
        )
