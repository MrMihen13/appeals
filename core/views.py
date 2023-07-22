from rest_framework import generics, permissions, pagination, response, status
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from core.models import Appeal
from core.serializers import CreateAppealSerializer, AppealSerializer
from core.permissions import IsOwner
from core.filters import AppealFilter


class CreateAppealAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateAppealSerializer
    queryset = Appeal.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        data['owner'] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListAppealsAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AppealSerializer
    queryset = Appeal.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AppealFilter
    search_fields = ['title', 'auditorium']
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('created_at').all()


class RetrieveUpdateDeleteAppealAPIVew(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AppealSerializer
    queryset = Appeal.objects.all()
