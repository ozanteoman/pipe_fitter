from rest_framework import serializers
from project_app.models import Topic

from admin_api.serializers.order import OrderDetailSerializer
from admin_api.serializers.service import ServiceSerializer


class ChangeTopicStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['status']


class TopicSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    order = OrderDetailSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ['service', 'full_name', 'phone_number', 'title', 'description', 'address', 'created_at', 'status', 'order']


class TopicEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['full_name', 'phone_number', 'title', 'description', 'address']
