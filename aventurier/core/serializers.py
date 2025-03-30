from rest_framework import serializers
from core.models import VocabItem


class VocabItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabItem
        fields = "__all__"
