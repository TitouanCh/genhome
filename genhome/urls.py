from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('annotate/<int:sequence_id>/', views.annotate_sequence, name='annotate_sequence'),
    path('annotation/delete/<int:annotation_id>/', views.delete_annotation, name='delete_annotation'),
    path('add-sequence/', views.add_sequence, name='add_sequence'),
]
