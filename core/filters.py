from django_filters.rest_framework import FilterSet

from core.models import Appeal


class AppealFilter(FilterSet):
    class Meta:
        model = Appeal
        fields = ['group', 'status', 'priority']
