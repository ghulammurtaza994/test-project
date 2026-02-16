from zipfile import Path
from django.urls import path, include
from . import views
from rest_framework import routers
from finalapp.views import InstructorViewSet    

router = routers.DefaultRouter()
router.register(r'instructors', InstructorViewSet)


router.register(r'courses', views.CourseViewSet)



urlpatterns = [

    path('', views.index, name='index'),   
    path('home', views.home, name='home'),
    path('', include(router.urls)),
    
    




]