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
    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255)
    part_number = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    specifications = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=8, choices=[('Valid', 'Valid'), ('Obsolete', 'Obsolete')])
    contact_email = models.EmailField(null=True,blank=True)
    documentation_url = models.URLField(null=True,blank=True)
    equivalent_id = models.IntegerField(null=True,blank=True)
    comments = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # New fields
    characteristics = models.JSONField(null=True, blank=True)
    performance = models.JSONField(null=True, blank=True)
    physical = models.JSONField(null=True, blank=True)
    input_output = models.JSONField(null=True, blank=True)
    software = models.JSONField(null=True, blank=True)
    other = models.JSONField(null=True, blank=True)
    display = models.JSONField(null=True, blank=True)
    bandwidth = models.CharField(max_length=255, null=True, blank=True)
    channels = models.CharField(max_length=255, null=True, blank=True)
    sample_rate = models.CharField(max_length=255, null=True, blank=True)
    record_length = models.CharField(max_length=255, null=True, blank=True)
    vertical_resolution = models.CharField(max_length=255, null=True, blank=True)
    vertical_sensitivity = models.CharField(max_length=255, null=True, blank=True)
    dc_vertical_accuracy = models.CharField(max_length=255, null=True, blank=True)
    max_input_voltage = models.CharField(max_length=255, null=True, blank=True)
    time_base_range = models.CharField(max_length=255, null=True, blank=True)
    time_base_accuracy = models.CharField(max_length=255, null=True, blank=True)
    horizontal_zoom = models.CharField(max_length=255, null=True, blank=True)
    io_interfaces = models.JSONField(null=True, blank=True)
    acquisition_modes = models.JSONField(null=True, blank=True)
    trigger_system = models.JSONField(null=True, blank=True)
    cursors = models.JSONField(null=True, blank=True)
    automatic_waveform_measurements = models.JSONField(null=True, blank=True)
    waveform_math = models.JSONField(null=True, blank=True)
    autoset_menu = models.JSONField(null=True, blank=True)
    display_characteristics = models.JSONField(null=True, blank=True)
    environmental_safety = models.JSONField(null=True, blank=True)
    frequency_range = models.CharField(max_length=255, null=True, blank=True)
    voltage_reference = models.CharField(max_length=255, null=True, blank=True)
    output_voltage_range = models.CharField(max_length=255, null=True, blank=True)
    output_current = models.CharField(max_length=255, null=True, blank=True)
    current_limit = models.CharField(max_length=255, null=True, blank=True)
    line_regulation = models.CharField(max_length=255, null=True, blank=True)
    constant_current_range = models.CharField(max_length=255, null=True, blank=True)
    current_accuracy = models.CharField(max_length=255, null=True, blank=True)
    max_voltage_power = models.CharField(max_length=255, null=True, blank=True)
    short_circuit_current = models.CharField(max_length=255, null=True, blank=True)
    measurement_accuracy = models.JSONField(null=True, blank=True)
    voltage_range = models.CharField(max_length=255, null=True, blank=True)
    resolution = models.CharField(max_length=255, null=True, blank=True)
    accuracy = models.CharField(max_length=255, null=True, blank=True)
    dc_voltage_measurement = models.CharField(max_length=255, null=True, blank=True)
    ac_voltage_measurement = models.CharField(max_length=255, null=True, blank=True)
    signal_sampling = models.JSONField(null=True, blank=True)
    frequency_measurement_range = models.CharField(max_length=255, null=True, blank=True)
    amplitude_range = models.JSONField(null=True, blank=True)
    offset_range = models.JSONField(null=True, blank=True)
    sine_distortion = models.JSONField(null=True, blank=True)
    pulse_width = models.JSONField(null=True, blank=True)
    angle_range = models.CharField(max_length=255, null=True, blank=True)
    reference_input = models.JSONField(null=True, blank=True)
    output_characteristics = models.JSONField(null=True, blank=True)
    angle_measurement_range = models.CharField(max_length=255, null=True, blank=True)
    input_characteristics = models.JSONField(null=True, blank=True)
    wavelength_range = models.CharField(max_length=255, null=True, blank=True)
    attenuation_range = models.CharField(max_length=255, null=True, blank=True)
    insertion_loss = models.CharField(max_length=255, null=True, blank=True)
    fibre_type = models.CharField(max_length=255, null=True, blank=True)
    connector_type = models.CharField(max_length=255, null=True, blank=True)
    bidirectional_switch = models.BooleanField(null=True, blank=True)
    power_range = models.CharField(max_length=255, null=True, blank=True)
    interface = models.JSONField(null=True, blank=True)
    parameters = models.JSONField(null=True, blank=True)
    pattern = models.JSONField(null=True, blank=True)
    pressure_supply = models.CharField(max_length=255, null=True, blank=True)
    vacuum_supply = models.CharField(max_length=255, null=True, blank=True)
    input_output_ports = models.JSONField(null=True, blank=True)
    pressure_range = models.JSONField(null=True, blank=True)
    pressure_generation_measurement = models.JSONField(null=True, blank=True)

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