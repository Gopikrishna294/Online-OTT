from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('register',registration,name='register'),
    path('login',mylogin,name='login'),
    path('logout',mylogout,name='logout'),
]
