from django.urls import path
from course.views import ListCourse,ListSubjects,ListSemesters
urlpatterns = [
    path("",ListCourse.as_view(),name="list-courses"),
    path("semester",ListSemesters.as_view(),name="list-semesters"),
    path("subject",ListSubjects.as_view(),name="list-subjects"),
]
