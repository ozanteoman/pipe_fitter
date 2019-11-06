from rest_framework import serializers

from project_app.models import Order


class OrderDetailSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['user', 'topic', 'price', 'status']

    def get_topic(self, obj):
        from admin_api.serializers.topic import TopicSerializer
        return TopicSerializer(instance=obj.topic, read_only=True).data


class CompleteOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status', 'price']


class UpdateOrderPriceSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(min_value=0, required=True)

    class Meta:
        model = Order
        fields = ['price']
