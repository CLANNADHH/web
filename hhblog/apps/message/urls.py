from django.conf.urls import url

from message import views

urlpatterns = [
    url(r'$', views.MessageView.as_view())
]