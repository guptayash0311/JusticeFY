from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Lawyer
from .models import Cases
from .serializer import LawyerSerializer
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


@api_view(['GET'])
def getLawyers(request):
    if request.user.is_authenticated:
        lawyers = Lawyer.objects.all()
        serializer = LawyerSerializer(lawyers, many=True)
        return Response(serializer.data)
    else:
        return HttpResponse("Login Required")
        



def createUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        id = request.POST.get("id")
        user = User.objects.create_user(
            username=username, email=email, password=password)
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
        return redirect("/api/login/")
    return render(request,'register.html')



def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username, password=password)
        if user is not None:
            print(user)
            print("User Groups:", user.groups.all())
            if user.groups.filter(name='Lawyers').exists():
                cases = Cases.objects.filter(Lawyer_Username=user.username)
                return render(request, 'lawyer_cart.html',{'cases': cases})
            elif user.groups.filter(name='Physical_Judge').exists():
                cases = Cases.objects.filter(Judge_Username=user.username)
                return render(request, 'Physical_Judge_Cart.html',{'cases': cases})
            elif user.groups.filter(name='Virtual_Judge').exists():
                return render(request, 'Virtual_Judge_Cart.html')
            else:
                return redirect('api/')
        else:
            return HttpResponse("Enter proper credentials")
    return render(request,'login.html')


@api_view(['POST'])
def logoutUser(request):
    logout(request)
    
def Home(request):
    return render(request,'index.html')


# @login_required
# def Cart(request):
#     user = request.user
#     if user.is_authenticated:
#         # print("Current User:", user)
#         # print("User Groups:", user.groups.all())
#         # if user.groups.filter(name='Lawyers').exists():
#         #     return render(request, 'lawyer_cart.html')
#         # elif user.groups.filter(name='Physical_Judge').exists():
#         #     return render(request, 'Physical_Judge_Cart.html')
#         # elif user.groups.filter(name='Virtual_Judge').exists():
#         #     return render(request, 'Virtual_Judge_Cart.html')
#         # else:
#         #     return redirect('api/')
#     else:
#         return redirect(reverse('api/login/'))
    
