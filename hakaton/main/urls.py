from django.urls import path
from . import views
from .views import register


urlpatterns = [
    path('', views.index),
    path("sport", views.sport),
    path("climat", views.climat),
    path("register", views.register, name='register'),
    path("water", views.water),
    path("ural", views.ural),
    path("sakmara", views.sakmara),
    path("geogr", views.geogr),

]
