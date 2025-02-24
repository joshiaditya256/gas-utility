

from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'service_type', 'status', 'created_at', 'updated_at')
    list_filter = ('service_type', 'status', 'created_at')
    search_fields = ('customer__username', 'description')

