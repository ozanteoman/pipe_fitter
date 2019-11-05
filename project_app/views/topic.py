from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from project_app.models import Topic
from project_app.serializers import TopicCreateSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    http_method_names = ['post', 'patch', 'head', 'options', 'trace']
    permission_classes = [AllowAny]
    serializer_class = TopicCreateSerializer
