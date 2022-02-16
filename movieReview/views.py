from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from .forms import MovieForm
from .models import Movie
from django.urls import reverse_lazy

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movieReview/addfood.html'
    success_url = reverse_lazy('movielist')

class MovieListView(ListView):
    model = Movie
    context_object_name = 'movielist'
    template_name = 'movieReview/foodlist.html'

class UpdateMovieView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movieReview/updatefood.html'
    success_url = reverse_lazy('movielist')

class DeleteMovieView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movielist')

def watch(req):
    return HttpResponse('<h1>If you wants to watch full movie go to pro</h1>')
