from rest_framework import serializers
from .models import Course, Instructor, Student  


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(source='Instructor', read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'Instructor', 'instructor']


class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True, required=False)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        write_only=True,
        required=True,
        source='course'
    )
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'enrollment_number', 'course', 'course_id']