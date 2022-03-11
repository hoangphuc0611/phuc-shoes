from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import load_all, create_cartitem,subtract,addition,remove

urlpatterns = [
    path('', load_all, name='load_all'),
    path('create_cartitem/<str:pk>', create_cartitem, name="create_cartitem"),
    path('subtract/<str:id>', subtract, name="subtract"),
    path('add/<str:id>', addition, name="addition"),
    path('remove/<str:id>', remove, name="remove"),
]