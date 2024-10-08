from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.get_notes, name='get_notes'),
    path('notes/create', views.create_note, name='create_note'),
    path('notes/<int:pk>', views.note_detail, name='note_detail')
]
