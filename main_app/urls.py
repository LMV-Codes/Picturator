from django.urls import path
from .views import HomePageView, ImageListView, ImageDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('images/', ImageListView.as_view(), name="list_view"),
    path('<uuid:pk>', ImageDetailView.as_view(), name="detail_view"),
]
