from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from .models import Conversation, Message, AccessRequest, Instrument, Equivalent, InstrumentFeature, File,CustomUser
from .serializers import CustomUserSerializer, ConversationSerializer, MessageSerializer, AccessRequestSerializer, InstrumentSerializer, EquivalentSerializer, InstrumentFeatureSerializer, FileSerializer
from rest_framework import viewsets


class TestConnectionAPI(APIView):
    """
    Test API for checking the connectivity of the chatbot service.
    """
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        return Response({'status': 'success', 'message': 'Chatbot API is reachable'}, status=status.HTTP_200_OK)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class AccessRequestViewSet(viewsets.ModelViewSet):
    queryset = AccessRequest.objects.all()
    serializer_class = AccessRequestSerializer
    permission_classes = [IsAuthenticated]

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [IsAuthenticated]

class EquivalentViewSet(viewsets.ModelViewSet):
    queryset = Equivalent.objects.all()
    serializer_class = EquivalentSerializer
    permission_classes = [IsAuthenticated]

class InstrumentFeatureViewSet(viewsets.ModelViewSet):
    queryset = InstrumentFeature.objects.all()
    serializer_class = InstrumentFeatureSerializer
    permission_classes = [IsAuthenticated]

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]