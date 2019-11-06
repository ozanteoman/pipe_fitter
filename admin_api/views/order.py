from rest_framework import viewsets
from rest_framework import status
from rest_framework import response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action

from project_app.models import Order
from project_app.choices import OrderStatus, TopicStatus
from admin_api.serializers import OrderDetailSerializer, CompleteOrderSerializer, UpdateOrderPriceSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, ]
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    @action(methods=["PUT"], detail=True, url_path="complete-order", serializer_class=CompleteOrderSerializer)
    def complete_order(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()

        price = request.data.get('price', '') or obj.topic.service.price  # if price is none , assign service price
        data = {'price': price, 'status': OrderStatus.DONE}

        serializer = self.get_serializer(data)
        serializer.is_valid(raise_exception=True)

        obj = serializer.save()
        obj.topic.status = TopicStatus.DONE
        obj.topic.save()
        obj.save()

        serializer = OrderDetailSerializer(instance=obj)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=["PUT"], detail=True, url_path="update-price", serializer_class=UpdateOrderPriceSerializer)
    def update_price(self, request, pk=None, *args, **kwargs):
        return super(OrderViewSet, self).update(request, *args, **kwargs)
