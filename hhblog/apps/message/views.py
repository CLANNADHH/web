from time import strftime
import time
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

from message.models import VipMessage
from message.serializers import MessageSerializer


class MessageView(APIView):

    def get(self, request):
        message = VipMessage.objects.all()
        serializer = MessageSerializer(message,many=True)
        date_str = serializer.data[0].get("message_time")[:19]
        # date_str = "2016-11-30 13:53:59"
        s = time.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        # "2016-11-30 13:53:59"
        # time.strftime("%b %d %Y %H:%M:%S", )
        print(type(s),s)
        return Response(serializer.data)

    def post(self, request):

        serializer = MessageSerializer(data=request.data)
        serializer.is_valid()
        message = serializer.save()
        # 2018-09-29 15:04:34.380000+00:00
        return Response()
