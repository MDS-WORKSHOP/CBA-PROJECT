from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class TestConnectionAPI(APIView):
    """
    Test API for checking the connectivity of the chatbot service.
    """
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        return Response({'status': 'success', 'message': 'Chatbot API is reachable'}, status=status.HTTP_200_OK)
