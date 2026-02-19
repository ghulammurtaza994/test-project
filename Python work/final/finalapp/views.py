from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Instructor, Student, Course
from .serializers import InstructorSerializer, StudentSerializer, CourseSerializer








class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')

def tryview(request):
    return render(request, 'try.html')  

def home(request):
    return render(request, 'Home.html')

def instructors_view(request):
    return render(request, 'instructors.html')

