from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from project_app.models import Service
from project_app.serializers import ServiceSerializer


class ServiceViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Service.objects.active()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny, ]
