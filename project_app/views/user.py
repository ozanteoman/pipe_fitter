from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)
from project_app.models import User

from project_app.serializers import (
    ChangeProfilePhotoSerializer,
    UserBasicInfoSerializer
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserBasicInfoSerializer

    def get_object(self):
        if self.action == "change_profile_image":
            # don't need to get object from db
            self.check_object_permissions(self.request, self.request.user)
            return self.request.user
        return super(UserViewSet, self).get_object()

    @action(methods=["PUT"], detail=False, serializer_class=ChangeProfilePhotoSerializer,
            url_path="change-profile-image", parser_classes=[MultiPartParser, ])
    def change_profile_image(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
