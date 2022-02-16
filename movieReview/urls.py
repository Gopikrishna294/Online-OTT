from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='movieReview/index.html'),name='Home'),
    path('addfood',MovieCreateView.as_view(),name='addmovie'),
    path('showfood',MovieListView.as_view(),name='movielist'),
    path('deletefood/<pk>',DeleteMovieView.as_view(),name='deletemovie'),
    path('updatefood/<pk>',UpdateMovieView.as_view(),name='updatemovie'),
    path('watch',watch)
]
