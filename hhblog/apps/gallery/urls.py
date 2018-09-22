from django.conf.urls import url
from . import views

# namespace
app_name = 'gallery'

urlpatterns = [

    url(r'^album/$', views.AlbumListView.as_view(), name='album_list'),
    url(r'^album/(?P<pk>\d+)/(?P<slug1>[-\w]+)/$', views.AlbumDetail.as_view(), name='album_detail'),

]