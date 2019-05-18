from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='myapp-Home Page'),
    path('upload/', views.upload, name='upload'),

]