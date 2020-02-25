
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homepage, name = 'homepage'),
    path("<item_id>", views.item, name = 'item')
]
