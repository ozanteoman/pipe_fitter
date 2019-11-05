from rest_framework import serializers

from project_app.models import Order


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'topic', 'price', 'status']
