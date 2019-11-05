from django.contrib.auth.models import AbstractUser
from django.db import models
from project_app.choices import UserType


class User(AbstractUser):
    image = models.ImageField(verbose_name="profile_picture", null=True)
    birthday = models.DateField(null=True)
    user_type = models.IntegerField(choices=UserType.STATUS, default=1)

    def __str__(self):
        return self.username

    @property
    def get_image_or_default(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/sample.jpg'
