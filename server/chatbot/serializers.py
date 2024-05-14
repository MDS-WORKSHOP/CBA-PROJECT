from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Conversation, Message, Request, Instrument, Equivalent, InstrumentFeature, File

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class EquivalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equivalent
        fields = '__all__'

class InstrumentFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentFeature
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
