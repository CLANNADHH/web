from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serialilzers import RegisterSerializer
from .models import User


class RegisterUsernameCountAPIView(APIView):
    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        context = {
            'count': count,
            'username': username
        }
        return Response(context)


class RegisterMobileCountAPIView(APIView):
    def get(self, request, mobile):
        count = User.objects.filter(mobile=mobile).count()
        context = {
            'count': count,
            'mobile': mobile
        }
        return Response(context)


class RegisterCreateView(APIView):
    # serializer_class = RegisterSerializer
    def post(self,request):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid()
        print(serializer.errors)
        userinfo = serializer.save()
        # print(userinfo)
        # return Response(userinfo.data)
        return Response()


class LoginView(APIView):
    def post(self,request):
        print(request.data)
        return Response()