from rest_framework import serializers
from mcq.models import Option,Question

class OptionSerialier(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
        depth = 1

class QuestionSerialier(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
     