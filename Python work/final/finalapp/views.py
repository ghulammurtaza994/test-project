from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Instructor
from .serializers import InstructorSerializer
from .models import Course
from .serializers import Courseserializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = Courseserializer
    

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tryview(request):
    return render(request, 'try.html')  

def home(request):
    return render(request, 'Home.html')

