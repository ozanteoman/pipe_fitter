from django.urls import path, re_path
from django.conf.urls import include

from rest_framework import routers

from project_app.views import *

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
