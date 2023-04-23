from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from course.serializers import CourseSerialier,SubjectSerialier,SemesterSerialier

from course.models import Course,Subject,Semester

class ListCourse(ListAPIView):
    serializer_class = CourseSerialier
    queryset = Course.objects.all()

class ListSubjects(ListAPIView):
    serializer_class = SubjectSerialier
    queryset = Subject.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['semester']
    

class ListSemesters(ListAPIView):
    serializer_class = SemesterSerialier
    queryset = Semester.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']