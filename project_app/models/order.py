from django.db import models

from project_app.choices import OrderStatus


class Order(models.Model):
    user = models.ForeignKey(to="project_app.User", null=True, blank=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(to="project_app.Topic", on_delete=models.CASCADE, null=False, blank=False)
    price = models.PositiveIntegerField(default=0, blank=True)
    status = models.IntegerField(choices=OrderStatus.STATUS, default=OrderStatus.ACTIVE)

    def __str__(self):
        return f"{self.user.username}-{self.status}"
