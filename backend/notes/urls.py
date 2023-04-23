from django.urls import path
from notes.views import CreateListNotes

urlpatterns = [
    path('', CreateListNotes.as_view(), name='create-list-notes'),
]
