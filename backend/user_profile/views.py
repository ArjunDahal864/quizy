from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from user_profile.permissions import UserIsAuthor
from rest_framework.views import APIView

class CreateProfileView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated,UserIsAuthor]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    
      
       
