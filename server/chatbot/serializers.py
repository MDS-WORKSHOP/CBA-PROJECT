from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Conversation, Message, AccessRequest, Instrument, Equivalent, InstrumentFeature, File, CustomUser , PasswordReset
from django.utils import timezone
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'id', 'password', 'first_name', 'last_name', 'email', 'access_id', 'profile', 'role', 'site', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = CustomUser.objects.create_user(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                access_id=validated_data['access_id'],
                profile=validated_data['profile'],
                role=validated_data.get('role', 'user'),
                site=validated_data['site'],
                password=validated_data['password']
            )
            return user
        except Exception as e:
            print(e)
            raise serializers.ValidationError({'error': str(e)})

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

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = CustomUser.objects.get(email=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.get(email=validated_data['email'])
        reset_token = PasswordReset.objects.create(user=user)
        print("reset_token:",reset_token)
        reset_url = f"{settings.FRONTEND_URL}/reset-password?token={reset_token.token}"
        
        # Render the HTML template
        html_content = render_to_string('password_reset_email.html', {'reset_url': reset_url})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            'Password Reset Request',
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        
        return reset_token

class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.UUIDField()
    new_password = serializers.CharField(write_only=True)

    def validate_token(self, value):
        try:
            reset_request = PasswordReset.objects.get(token=value)
        except PasswordReset.DoesNotExist:
            raise serializers.ValidationError("Invalid token.")
        
        if reset_request.is_expired():
            raise serializers.ValidationError("Token has expired.")
        
        return value

    def save(self, validated_data):
        token = validated_data['token']
        new_password = validated_data['new_password']
        reset_request = PasswordReset.objects.get(token=token)
        user = reset_request.user
        user.set_password(new_password)
        user.save()
        reset_request.delete()

class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordReset
        fields = ['id', 'user', 'token', 'created_at', 'expiration_time']

    def create(self, validated_data):
        expiration_time = validated_data.get('expiration_time', timezone.now() + settings.PASSWORD_RESET_EXPIRATION_TIME)
        password_reset = PasswordReset.objects.create(
            user=validated_data['user'],
            token=validated_data['token'],
            expiration_time=expiration_time
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

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("No user with this email found.")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password.")

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)

            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        raise serializers.ValidationError("Unable to log in with provided credentials.")