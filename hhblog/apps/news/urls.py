from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create', views.NewsCreate.as_view()),
    url(r'^$', views.NewView.as_view()),
]