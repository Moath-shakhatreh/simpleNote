from django.urls import path ,include
from simplenote_app.api.views import NoteListView, NoteDetailView

urlpatterns = [
    path('notes/', NoteListView.as_view() , name='note_list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]