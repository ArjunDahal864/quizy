from django.urls import path,re_path
from mcq.views import ListOptions,ListQuestions,ListMcqAnswers,CreateMcqAnswers
urlpatterns = [
    path("",ListQuestions.as_view(),name="list-questions"),
    path("options/<int:question>",ListOptions.as_view(),name="list-questions"),
    path("answer",CreateMcqAnswers.as_view(),name="list-my-answers"),
    path("my-answers",ListMcqAnswers.as_view(),name="list-my-answers"),

]
