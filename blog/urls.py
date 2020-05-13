from django.urls import path
from . views import post_view, like_post

app_name = "blog"
urlpatterns = [
    path('', post_view, name="index"),
    path('like/', like_post, name = "like"),
]
