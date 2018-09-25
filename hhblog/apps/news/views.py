from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from until import get_news


class NewView(APIView):
    def get(self, request):

        news = get_news.catch_news(1)
        return Response(news.parse_news())
