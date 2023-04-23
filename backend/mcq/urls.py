from django.urls import path,re_path
from mcq.views import ListOptions,ListQuestions
urlpatterns = [
    path("",ListQuestions.as_view(),name="list-questions"),
    path("options/<int:question>",ListOptions.as_view(),name="list-questions"),
]
