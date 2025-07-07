from django.urls import path

from . import views


urlpatterns = [
    path('reviews/', views.ReviewListView.as_view(), name="reviews_create_list"),
    path('reviews/<int:pk>', views.ReviewRetrieveUpdateDestroyView.as_view(), name="reviews_detail_view"),
]
