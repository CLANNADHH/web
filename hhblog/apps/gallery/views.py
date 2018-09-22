import json

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from gallery.serializers import Galleryserializer
from .models import Album, AlbumImage


class AlbumListView(APIView):

    queryset = Album.objects.filter(is_visible=True).order_by("-create_date")
    paginate_by = 1

    def get(self, request):
        album = Album.objects.get(id=1)
        # return Response(json.dumps({'album':album}))
        serializers = Galleryserializer(album)
        return Response(serializers.data)


class AlbumDetail(DetailView):
    model = Album

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context
