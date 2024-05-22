from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("page2", views.page2, name="page2"),
]
