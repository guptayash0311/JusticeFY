from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Lawyer
from .serializer import LawyerSerializer
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, logout

# Create your views here.


@api_view(['GET'])
def getLawyers(request):
    lawyers = Lawyer.objects.all()
    serializer = LawyerSerializer(lawyers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createUser(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    id = request.POST.get("id")
    user = User.objects.create_user(
        username=username, email=email, password=password)
    # print(name, email, password)
    # print(request.POST)
    if (id == "1"):
        Lawyers = Group.objects.get(id='1')
        Lawyers.user_set.add(user)
    if (id == "2"):
        Physical_Judge = Group.objects.get(id='2')
        Physical_Judge.user_set.add(user)
    if (id == "3"):
        Virtual_Judge = Group.objects.get(id='3')
        Virtual_Judge.user_set.add(user)
    user.save()
    return HttpResponse("User registered successfully")


@api_view(['POST'])
def loginUser(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request,username=username, password=password)
    if user is not None:
        return HttpResponse("User Logged in successfully")
    else:
        return HttpResponse("Enter proper credentials")


@api_view(['POST'])
def logoutUser(request):
    logout(request)
