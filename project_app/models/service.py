from django.db import models

from project_app.choices import ServiceStatus


class ServiceManager(models.Manager):

    def active(self):
        return self.filter(status=ServiceStatus.ACTIVE)

    def staff_visible(self):
        # only staff user can see  ACTIVE and INACTIVE
        return self.filter(status__in=[ServiceStatus.ACTIVE, ServiceStatus.INACTIVE])


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Service Title", null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.IntegerField(choices=ServiceStatus.STATUS, default=ServiceStatus.ACTIVE)
    price = models.PositiveIntegerField(default=0, blank=True, null=False)

    objects = ServiceManager()

    def __str__(self):
        return self.title
