from rest_framework import generics, permissions

from core.models import Appeal
from core.serializers import CreateAppealSerializer, AppealSerializer
from core.permissions import IsOwner


class CreateAppealAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateAppealSerializer
    queryset = Appeal.objects.all()


class ListAppealsAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AppealSerializer
    queryset = Appeal.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).all()


class RetrieveUpdateDeleteAppealAPIVew(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AppealSerializer
    queryset = Appeal.objects.all()
