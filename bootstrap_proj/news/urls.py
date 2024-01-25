
from django.contrib import admin
from django.urls import path, include
from . views import index, details

urlpatterns = [
    path('', index, name="index"),
    path('<int:id>/', details, name="details")
]
