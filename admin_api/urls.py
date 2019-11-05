from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from admin_api.views import ServiceViewSet, TopicViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('services', ServiceViewSet)
router.register('topic', TopicViewSet)

urlpatterns = [
    path('', include(router.urls))
]
