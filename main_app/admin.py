from django.contrib import admin
from main_app.models import Company, Contact, Service, ServiceRequest


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'employees', 'started']
    list_filter = ['started', ]
    search_fields = ['name', 'type', 'employees', 'about_us']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'call_back', 'created']
    list_filter = ['call_back', 'created', 'updated']
    search_fields = ['full_name', 'email', 'phone']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'display']
    list_filter = ['display', ]
    search_fields = ['name', 'description']


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'call_back', 'parent_service']
    list_filter = ['call_back', 'parent_service', 'created']
    search_fields = ['full_name', 'email', 'phone_number', 'message']
