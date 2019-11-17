from rest_framework import serializers
from project_app.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()

    class Meta:
        model = Service
        fields = ['id','title', 'price', 'status', 'created_at', 'updated_at']
