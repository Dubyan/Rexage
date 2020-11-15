from django.urls import path
from . import views
from django.conf.urls import include, url


urlpatterns = [
    path('', views.index),
    path("sport", views.sport),
    path("climat", views.climat),
    path("water", views.water),
    path("ural", views.ural),
    path("sakmara", views.sakmara),
    path("geogr", views.geogr),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    path("maps", views.maps),
    path("list", views.list),
    path("create", views.create),
    path("pal", views.pal),
    path("gl", views.gl),
    path("kuv", views.kuv)

]
