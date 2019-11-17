from rest_framework import serializers
from project_app.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'slug', 'price', 'status', 'created_at', 'updated_at']
