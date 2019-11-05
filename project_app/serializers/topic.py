from rest_framework import serializers

from project_app.models import Topic


class TopicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'full_name', 'phone_number', 'service', 'address']
