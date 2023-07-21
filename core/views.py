from rest_framework import generics, permissions, pagination

from django_filters.rest_framework import DjangoFilterBackend

from core.models import Appeal
from core.serializers import CreateAppealSerializer, AppealSerializer
from core.permissions import IsOwner
from core.filters import AppealFilter


class CreateAppealAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateAppealSerializer
    queryset = Appeal.objects.all()


class ListAppealsAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AppealSerializer
    queryset = Appeal.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = AppealFilter
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).order_by('created_at').all()


class RetrieveUpdateDeleteAppealAPIVew(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AppealSerializer
    queryset = Appeal.objects.all()
