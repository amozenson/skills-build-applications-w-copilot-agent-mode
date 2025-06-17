from django.urls import path
from .views import FitnessEntryListCreateView, FitnessEntryDetailView

urlpatterns = [
    path('fitness/', FitnessEntryListCreateView.as_view(), name='fitness-list-create'),
    path('fitness/<int:pk>/', FitnessEntryDetailView.as_view(), name='fitness-detail'),
]
