from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action
from rest_framework import response
from rest_framework import status

from admin_api.serializers import ServiceSerializer

from project_app.models import Service
from project_app.choices import ServiceStatus


class ServiceViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options', 'trace']
    permission_classes = [IsAdminUser, ]
    queryset = Service.objects.staff_visible()
    serializer_class = ServiceSerializer

    @action(methods=['put'], detail=True, url_path="delete-service")
    def delete_service(self, request, pk=None):
        obj = self.get_object()
        obj.status = ServiceStatus.DELETED
        obj.save()
        return response.Response(data={'message': "deleted"}, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, url_path="change-status/<str:status_value>/")
    def change_status(self, request, pk=None, status_value=None):
        allowed_situations = [ServiceStatus.INACTIVE, ServiceStatus.ACTIVE]
        if status_value not in allowed_situations:
            raise ValidationError({'status_error': "Böyle bir durum bulunamadı."})

        obj = self.get_object()
        obj.status = status_value
        obj.save()

        return response.Response(data={'message': "status changed successfully"}, status=status.HTTP_200_OK)
