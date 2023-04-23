from rest_framework import serializers
from course.models import Course,Subject,Semester

class CourseSerialier(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class SubjectSerialier(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SemesterSerialier(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'
     
