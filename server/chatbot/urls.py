from django.urls import path, include
from .views import TestConnectionAPI
from .views import  CustomUserViewSet, ConversationViewSet, MessageViewSet, AccessRequestViewSet, InstrumentViewSet, EquivalentViewSet, InstrumentFeatureViewSet, FileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'access_requests', AccessRequestViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'equivalents', EquivalentViewSet)
router.register(r'instrument_features', InstrumentFeatureViewSet)
router.register(r'files', FileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('test/', TestConnectionAPI.as_view(), name='test-connection'),
]