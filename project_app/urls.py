from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from project_app.views import *

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'topic', TopicViewSet)

urlpatterns = [
    path('', include(router.urls))
]
