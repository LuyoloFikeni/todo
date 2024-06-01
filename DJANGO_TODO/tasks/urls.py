from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('update/<int:id>/', views.update, name='update'),
    ]