from django.contrib import admin
from django.urls import path, include

print("""
Admin: http://127.0.0.1:8000/admin
actors: http://127.0.0.1:8000/api/v1/actors/
genres: http://127.0.0.1:8000/api/v1/genres/
movies: http://127.0.0.1:8000/api/v1/movies/
reviews: http://127.0.0.1:8000/api/v1/reviews/
""")


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),  
    path('api/v1/', include('actors.urls')),  
    path('api/v1/', include('genres.urls')),  
    path('api/v1/', include('movies.urls')),  
    path('api/v1/', include('reviews.urls')),  
]
