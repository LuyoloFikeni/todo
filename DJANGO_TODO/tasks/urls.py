from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('update/<int:pk>/', views.update, name='update'),
    ]