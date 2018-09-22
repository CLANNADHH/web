from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^(?P<pk>\d+)$',views.BlogView.as_view()),
    url(r'^list$',views.BlogListView.as_view()),

]