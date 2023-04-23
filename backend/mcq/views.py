from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from mcq.serializers import OptionSerialier,QuestionSerialier,McqAnswerSerialier,McqAnswerDepthSerialier
from mcq.models import Option,Question,MCQAnswers

# Create your views here.
class ListOptions(ListAPIView):
    serializer_class = OptionSerialier
    queryset = Option.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question']

    def get_queryset(self):
        return self.queryset.all().filter(question=self.kwargs['question'])
    
class ListQuestions(ListAPIView):
    serializer_class = QuestionSerialier
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject']

class ListMcqAnswers(ListAPIView):
    serializer_class = McqAnswerDepthSerialier
    queryset = MCQAnswers.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def get_queryset(self):
        return self.queryset.all().filter(user=self.request.user)
        


class CreateMcqAnswers(CreateAPIView):
    serializer_class = McqAnswerSerialier
    queryset = MCQAnswers.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
