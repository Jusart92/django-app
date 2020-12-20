""" URLs modeule"""
from django.urls import path
from djangoGram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sorted_numbers),
    path('hi/<str:name>/<int:age>', local_views.say_hi),

    path('posts/', posts_views.list_posts),
]