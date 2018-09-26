from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from news.crons import generate_news_file
from until import get_news


class NewView(APIView):
    def get(self, request):

        news = get_news.CatchNews(1)
        return Response(news.parse_news())


class NewsCreate(APIView):
    def get(self, request):
        generate_news_file()
        return Response()