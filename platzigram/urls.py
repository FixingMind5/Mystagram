"""URL'S modules of platzigram"""
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
from platzigram import views
from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', views.hola_mundo, name='hello_world'),
    path('sorted/', views.sorted_integers, name='sort'),
    path('hi/<str:name>/<int:age>/', views.say_hi, name='hi'),

    path('posts/', posts_views.lists_posts, name='feed'),

    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup', users_views.sign_up, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
