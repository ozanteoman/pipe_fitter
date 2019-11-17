from django.db import models
from unidecode import unidecode
from django.template.defaultfilters import slugify


from project_app.choices import ServiceStatus


class ServiceManager(models.Manager):

    def active(self):
        return self.filter(status=ServiceStatus.ACTIVE)

    def staff_visible(self):
        # only staff user can see  ACTIVE and INACTIVE
        return self.filter(status__in=[ServiceStatus.ACTIVE, ServiceStatus.INACTIVE])


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Service Title", null=False, blank=False)
    slug = models.SlugField(null=True, blank=False, max_length=104)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.IntegerField(choices=ServiceStatus.STATUS, default=ServiceStatus.ACTIVE)
    price = models.PositiveIntegerField(default=0, blank=True, null=False)

    objects = ServiceManager()

    def __str__(self):
        return self.title

    def _generate_unique_slug(self):
        count = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Service.objects.filter(slug=new_slug).exists():
            count += 1
            new_slug = f"{slug}-{count}"

        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = self._generate_unique_slug()
        super(Service, self).save(*args, **kwargs)
