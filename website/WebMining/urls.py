from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='myapp-Home Page'),
    path('upload/', views.upload, name='upload'),
    path('logs/', views.logfiles_list, name='logfiles_list'),
    path('logs/upload/', views.upload_log, name='upload_log'),

]