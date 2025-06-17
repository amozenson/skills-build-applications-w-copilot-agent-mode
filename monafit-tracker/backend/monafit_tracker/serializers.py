from rest_framework import serializers
from .models import FitnessEntry

class FitnessEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessEntry
        fields = '__all__'
