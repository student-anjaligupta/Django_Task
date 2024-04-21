from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('hello', views.hello_world),
    path("", views.home_page),
    path("all-analytics", views.All_analytics),
    path("analytics", views.Analytics),
    path("try", views.try_file),
    path("task", views.task_file)
]