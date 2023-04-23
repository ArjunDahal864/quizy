from rest_framework import serializers,exceptions
from user_profile.models import UserProfile



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['user',]
    
    def create(self, validated_data):
        if UserProfile.objects.filter(user=self.context['request'].user).exists():
            raise exceptions.NotAcceptable('User profile already exists')
        else:
            user_profile = UserProfile.objects.create(**validated_data)
            user_profile.save()
        return user_profile

    

