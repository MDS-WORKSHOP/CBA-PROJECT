from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
import uuid


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile = models.CharField(max_length=2, choices=[('CD', 'CD'), ('BT', 'BT')])
    role = models.CharField(max_length=5, choices=[('user', 'User'), ('admin', 'Admin')], default='user')
    email = models.EmailField(unique=True, null=False)
    site = models.CharField(max_length=3, choices=[('CDG', 'CDG'), ('VLR', 'VLR'), ('ORY', 'ORY')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Conversation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AccessRequest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile = models.CharField(max_length=2, choices=[('CD', 'CD'), ('BT', 'BT')])
    email = models.EmailField()
    site = models.CharField(max_length=3, choices=[('CDG', 'CDG'), ('VLR', 'VLR'), ('ORY', 'ORY')])
    reason = models.CharField(max_length=20, choices=[('authorization', 'Authorization'), ('password_reset', 'Password Reset')])
    status = models.CharField(max_length=8, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Instrument(models.Model):
    name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    specifications = models.TextField()
    status = models.CharField(max_length=8, choices=[('Valid', 'Valid'), ('Obsolete', 'Obsolete')])
    contact_email = models.EmailField()
    documentation_url = models.URLField()
    equivalent_id = models.IntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Equivalent(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

class InstrumentFeature(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=255)  # Feature name, e.g., "Bandwidth", "Sample Rate"
    value = models.CharField(max_length=255)  # Feature value
    unit = models.CharField(max_length=50)  # Unit of measurement, e.g., "MHz", "GS/s"

class Document(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='documents/')
    md5_hash = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PasswordReset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DateTimeField(default=timezone.now)

    def is_expired(self):
        return self.expiration_time < timezone.now()

    def save(self, *args, **kwargs):
        if not self.expiration_time:
            self.expiration_time = timezone.now() + settings.PASSWORD_RESET_EXPIRATION_TIME
        super().save(*args, **kwargs)  