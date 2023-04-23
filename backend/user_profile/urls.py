from django.urls import path
from user_profile.views import CreateProfileView

urlpatterns = [
    path('', CreateProfileView.as_view(), name='create-list'),
]
