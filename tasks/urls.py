from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='list_tasks'),
    path('update/<str:pk>/', views.update_task,name='update_task'),
    path('delete/<str:pk>/', views.delete_task,name='delete_task'),
    
    
]