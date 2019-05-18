from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logs/', views.logfiles_list, name='logfiles_list'),
    path('logs/upload/', views.upload_log, name='upload_log'),

]