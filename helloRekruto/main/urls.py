from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('comments', views.comments, name='comments'),
    path("url_name/", views.user, name='url'),
]