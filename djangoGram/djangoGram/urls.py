""" URLs modeule"""
from django.urls import path
from djangoGram import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('sorted/', views.sorted_numbers),
    path('hi/<str:name>/<int:age>', views.say_hi),
]
