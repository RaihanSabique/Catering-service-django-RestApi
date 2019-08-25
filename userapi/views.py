from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# from .models import User
# from .serializers import userSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

# class userList(APIView):
#     #permission_classes = (IsAuthenticated,)
#     def get(self,request):
#         users=User.objects.all()
#         serializer=userSerializer(users,many=True)
#         return Response(serializer.data)
#
#
# class CreateUserAPIView(APIView):
#     # Allow any user (authenticated or not) to access this url
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         user = request.data
#         serializer = userSerializer(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK
# )
#
# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     fb_token = request.data.get("facebook_access_token")
#     print(fb_token)
#     if fb_token is None :
#         return Response({'error': 'Please provide facebook access token'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = User.objects.filter(facebook_access_token=fb_token)
#     print(user)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)