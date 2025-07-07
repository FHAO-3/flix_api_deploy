from rest_framework import serializers
from django.db.models import Avg

from movies.models import Movie
from genres.models import Genre
from genres.seriliazers import GenresSerializer
from actors.models import Actor
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.Serializer):
    """
    Neste `Serializer` simples não tem como fazer um POST ou PUT nele, pois temos de implementar tudo à mão. Ele é o básico, feito para serializar os dados.
    O `Serializer` é uma classe que transforma os dados em JSON e vice-versa, mas não está pronto para fazer o CRUD, como por exemplo o POST, PUT.
    """
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
    )
    resume = serializers.CharField()


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year <= 1887:
            raise serializers.ValidationError('O ano de lançamento não pode ser anterior a 1887.')
        else:
            return value

    def validate_resume(self, value):
        if len(value) >= 1000:
            raise serializers.ValidationError('O resumo deve ter no maximo 1000 caracteres.')
        else:
            return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenresSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
