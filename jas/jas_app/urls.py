from django.urls import path
from . import views

urlpatterns = [
    path('index', views.home),
    path('sendMail', views.sendMail,name='sendMail'),
]