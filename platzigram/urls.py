"""URL'S modules of platzigram"""
from django.urls import path
from django.contrib import admin
from platzigram import views
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hola_mundo),
    path('sorted/', views.sorted_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi),
    path('posts/', posts_views.lists_posts),
]
