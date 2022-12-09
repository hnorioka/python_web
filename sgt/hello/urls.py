from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("seinao", views.seinao, name = "seinao"),
    path("naosei", views.naosei, name = "naosei")
]