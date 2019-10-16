from rest_framework import serializers

from project_app.models import User


class UserBasicInfoSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source="get_image_or_default")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'birthday', 'image']


class ChangeProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['image']
