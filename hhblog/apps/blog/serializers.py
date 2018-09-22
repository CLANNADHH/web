from rest_framework import serializers

from blog.models import MyBlog


class Blogserializer(serializers.ModelSerializer):

    class Meta():
        model = MyBlog
        fields = "__all__"