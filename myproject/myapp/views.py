# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

# Create a simple home view function
def home(request):
    return HttpResponse("Welcome to the API!")  # This will display a simple message when accessed

# Define the viewset for Person model
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
