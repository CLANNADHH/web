from rest_framework import serializers

from gallery.models import Album


class Galleryserializer(serializers.ModelSerializer):

    class Meta():
        model = Album
        fields = "__all__"