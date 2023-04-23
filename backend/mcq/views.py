from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from mcq.serializers import OptionSerialier,QuestionSerialier
from mcq.models import Option,Question

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