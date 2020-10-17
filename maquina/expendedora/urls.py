from django.urls import path
from . import views

app_name = "expendedora"

urlpatterns = [
    path('', views.index, name='index'),
    
]