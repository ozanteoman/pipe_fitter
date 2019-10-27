from rest_framework import serializers
from project_app.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["title", "price"]
