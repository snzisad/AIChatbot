from .models import ConversationHistory
from rest_framework import serializers


class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConversationHistory
        fields = ['token', 'message', 'response']