from rest_framework import generics
from .models import FitnessEntry
from .serializers import FitnessEntrySerializer

class FitnessEntryListCreateView(generics.ListCreateAPIView):
    queryset = FitnessEntry.objects.all()
    serializer_class = FitnessEntrySerializer

class FitnessEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FitnessEntry.objects.all()
    serializer_class = FitnessEntrySerializer
