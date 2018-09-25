from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.NewView.as_view()),
]