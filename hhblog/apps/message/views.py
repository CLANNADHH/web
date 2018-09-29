from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView


class MessageView(APIView):

    def post(self, request):
        print(request.POST.keys())
        return Response()
