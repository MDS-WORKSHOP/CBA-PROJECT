from django.urls import path
from .views import TestConnectionAPI



urlpatterns = [
    path('test/', TestConnectionAPI.as_view(), name='test-connection'),
]