

from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
        # Add other service types as needed
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_type} request by {self.customer.username} - {self.status}"

