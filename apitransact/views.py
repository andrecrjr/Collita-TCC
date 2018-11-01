from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .models import *
from .serializers import *

class NotaFiscalView(generics.ListCreateAPIView):
    queryset = NotaFiscalMoeda.objects.all()
    serializer_class = NotaFiscalSerializer