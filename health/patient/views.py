from django.shortcuts import render
from rest_framework import viewsets, status , mixins
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.
class PatientViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer