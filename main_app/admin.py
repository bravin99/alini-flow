from django.contrib import admin
from main_app.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'call_back', 'created']
    list_filter = ['call_back', 'created', 'updated']
    search_fields = ['full_name', 'email', 'phone']

