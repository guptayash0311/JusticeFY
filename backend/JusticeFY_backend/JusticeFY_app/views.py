from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Lawyer
from .serializer import LawyerSerializer

# Create your views here.
@api_view(['GET'])
def getLawyers(request):
    lawyers=Lawyer.objects.all()
    serializer=LawyerSerializer(lawyers, many=True)
    return Response(serializer.data)