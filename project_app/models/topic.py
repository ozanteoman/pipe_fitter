from django.db import models


from project_app.choices import TopicStatus, OrderStatus


class Topic(models.Model):
    service = models.ForeignKey('project_app.Service', null=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=False)
    address = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=TopicStatus.STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.full_name}" if self.full_name.strip("") != "" else f"{self.title}"

    @property
    def order(self):
        # exclude cancelled , because when order status was picking as cancelled , topic status will be `wating_for_assign`
        return self.order_set.exclude(status=OrderStatus.CANCELLED).first()
