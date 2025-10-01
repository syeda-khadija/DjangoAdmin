from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="reg"),
    path("l", views.Login, name="log"),
    path("h", views.home, name="home"),
    path("b", views.blog, name="blog"),
    path("bd", views.blog_details, name="blog_details"),
    path("sd", views.service_details, name="service_details"),
    path("s", views.service, name="ser"),
    path("p", views.pricing, name="pri"),
    path("c", views.contact, name="con"),

]