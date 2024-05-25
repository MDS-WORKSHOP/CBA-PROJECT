from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from .models import Conversation, Message, AccessRequest, Instrument, Equivalent, InstrumentFeature, File,CustomUser
from .serializers import CustomUserSerializer, ConversationSerializer, MessageSerializer, AccessRequestSerializer, InstrumentSerializer, EquivalentSerializer, InstrumentFeatureSerializer, FileSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from .serializers import PasswordResetRequestSerializer, PasswordResetConfirmSerializer
from .permissions import IsAdmin
from .utils import send_password_reset_email
from django.conf import settings
import uuid

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

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Password reset link sent.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail': 'Password has been reset.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AccessRequestCreateView(generics.CreateAPIView):
    queryset = AccessRequest.objects.all()
    serializer_class = AccessRequestSerializer

class AccessRequestListView(generics.ListAPIView):
    queryset = AccessRequest.objects.all()
    serializer_class = AccessRequestSerializer
    permission_classes = [IsAdmin]

class AccessRequestApproveView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request, pk):
        try:
            access_request = AccessRequest.objects.get(pk=pk)
            access_request.status = 'approved'
            access_request.save()
            
            # Générer un mot de passe par défaut
            default_password = str(uuid.uuid4())

            data = {
                'password': default_password,
                'email': access_request.email,
                'first_name': access_request.first_name,
                'last_name': access_request.last_name,
                'profile': access_request.profile,
                'site': access_request.site,
                'role': 'user',
            }
            
            # Utiliser le sérialiseur pour créer l'utilisateur
            user_serializer = CustomUserSerializer(data=data)
            if user_serializer.is_valid():
                user = user_serializer.save()

                # Envoyer un email pour réinitialiser le mot de passe
                reset_url = f"{settings.FRONTEND_URL}/reset-password"
                send_password_reset_email(user, reset_url)

                return Response({'detail': 'Access request approved and user created.'}, status=status.HTTP_200_OK)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except AccessRequest.DoesNotExist:
            return Response({'error': 'Access request not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class AccessRequestRejectView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request, pk):
        try:
            access_request = AccessRequest.objects.get(pk=pk)
            access_request.status = 'rejected'
            access_request.save()
            return Response({'detail': 'Access request rejected.'}, status=status.HTTP_200_OK)
        except AccessRequest.DoesNotExist:
            return Response({'error': 'Access request not found.'}, status=status.HTTP_404_NOT_FOUND)