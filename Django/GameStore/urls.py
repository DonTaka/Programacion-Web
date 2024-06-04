from django.urls import path
from GameStore import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crud", views.crud, name="crud"),
    path("user_add", views.user_add, name="user_add"),
]
