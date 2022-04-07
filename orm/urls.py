
from django.contrib import admin
from django.urls import path,include
from orm import views
urlpatterns = [
    path('task1/',views.task1),
    path('',views.task2)
]
