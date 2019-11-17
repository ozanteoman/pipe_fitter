from rest_framework import serializers
from project_app.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Service
        fields = ["id", "title", "price", "slug"]
