from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.RegisterUsernameCountAPIView.as_view()),
    url(r'^mobile/(?P<mobile>1[345789]\d{9})/count/$', views.RegisterMobileCountAPIView.as_view()),
    url(r'auths/$', views.LoginView.as_view()),
    url(r"",views.RegisterCreateView.as_view()),
]