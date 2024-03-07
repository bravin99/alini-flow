import uuid

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class MainAppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Company(MainAppBaseModel):
    name = models.CharField(max_length=65)
    type = models.CharField(max_length=65)
    employees = models.CharField(max_length=65)
    about_us = models.TextField()
    started = models.DateField()

    class Meta:
        verbose_name = 'Company Data'
        verbose_name_plural = 'Company Data'


class Contact(MainAppBaseModel):
    full_name = models.CharField(max_length=65)
    email = models.EmailField()
    phone = models.CharField(max_length=13, null=True, blank=True)
    message = models.TextField()
    call_back = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name}: {self.created}"

    class Meta:
        ordering = ('-created',)


class Service(MainAppBaseModel):
    name = models.CharField(max_length=165)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=9, null=True, blank=True)
    display = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()


class ServiceRequest(MainAppBaseModel):
    parent_service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_request')
    full_name = models.CharField(max_length=165)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField(help_text='Please provide any information relevant to the project here.')
    call_back = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service Request'
        verbose_name_plural = 'Service Requests'


class Subscriber(MainAppBaseModel):
    subscriber_hash = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    receive_emails = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.subscriber_hash:
            self.subscriber_hash = uuid.uuid4()
        return super().save()

