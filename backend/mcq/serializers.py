from rest_framework import serializers
from mcq.models import Option,Question,MCQAnswers

class OptionSerialier(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
        

class QuestionSerialier(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class McqAnswerSerialier(serializers.ModelSerializer):
    class Meta:
        model = MCQAnswers
        fields = ['question', 'option']     


class McqAnswerDepthSerialier(serializers.ModelSerializer):
    class Meta:
        model = MCQAnswers
        fields = ['question', 'option']
        depth = 1