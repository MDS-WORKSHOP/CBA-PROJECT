from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Conversation, Message, AccessRequest, Instrument, Equivalent, InstrumentFeature, File, CustomUser , PasswordReset
from django.utils import timezone
from django.conf import settings

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'password', 'first_name', 'last_name', 'email', 'access_id', 'profile', 'role', 'site', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            access_id=validated_data['access_id'],
            profile=validated_data['profile'],
            role=validated_data['role'],
            site=validated_data['site']
        )
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.access_id = validated_data.get('access_id', instance.access_id)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.role = validated_data.get('role', instance.role)
        instance.site = validated_data.get('site', instance.site)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordReset
        fields = ['id', 'user', 'token', 'created_at', 'expiration_time']

    def create(self, validated_data):
        password_reset = PasswordReset.objects.create(
            user=validated_data['user'],
            token=validated_data['token'],
            expiration_time=validated_data.get('expiration_time', timezone.now() + settings.PASSWORD_RESET_EXPIRATION_TIME)
        )
        return password_reset
    
class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class AccessRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRequest
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
