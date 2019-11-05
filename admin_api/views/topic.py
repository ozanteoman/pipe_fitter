from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import status
from rest_framework import response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action

from project_app.models import Topic, Order, User
from project_app.choices import OrderStatus

from admin_api.serializers import ChangeTopicStatusSerializer, TopicSerializer, TopicEditSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    permission_classes = [IsAdminUser, ]
    serializer_class = TopicSerializer

    @action(methods=["PUT"], detail=True, url_path="change-status", serializer_class=ChangeTopicStatusSerializer)
    def change_status(self, request, pk=None, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(methods=["GET"], detail=True, url_path="edit-topic", serializer_class=TopicEditSerializer)
    def edit_topic(self, request, pk=None, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(methods=["PUT"], detail=True, url_path="assign-user/<int:user_pk>", serializer_class=TopicSerializer)
    def assign_user(self, request, pk=None, user_pk=None, *args, **kwargs):
        obj = self.get_object()
        user = get_object_or_404(User, pk=user_pk)  # get object or raise 404 not found
        Order.objects.filter(topic=obj).update(status=OrderStatus.CANCELLED)  # mark as cancelled  before generate new order
        # generate new Order
        Order.objects.create(user_id=obj.id, topic_id=user.id, price=obj.service.price)
        serializer = self.get_serializer(instance=obj)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=["PUT"], detail=True, url_path="assign-place/<int:place-pk")
    def assign_place(self, ):
        pass
