from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import MyBlog
from blog.serializers import Blogserializer


# class BlogView(APIView):
#
#     def get(self, request):
#
#         blog = MyBlog.objects.get(id=1)
#
#         serializers = Blogserializer(blog)
#         return Response(serializers.data)

class BlogListView(ListModelMixin, GenericAPIView):

    # 限制查询集的个数
    queryset = MyBlog.objects.all()[0:6]
    serializer_class = Blogserializer

    def get(self,request):
        return self.list(request)


class BlogView(RetrieveModelMixin, GenericAPIView):
    serializer_class = Blogserializer
    queryset = MyBlog.objects.all()

    def get(self,request, pk):
        return self.retrieve(request,pk)

