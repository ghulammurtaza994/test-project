from rest_framework import serializers
from .models import Course, Instructor  


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'


class Courseserializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        