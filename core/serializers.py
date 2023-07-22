from rest_framework import serializers

from core.models import Appeal


class CreateAppealSerializer(serializers.ModelSerializer):
    body = serializers.CharField(source='markdown_body', write_only=True, label='Текст Обращения')

    class Meta:
        model = Appeal
        fields = ('title', 'auditorium', 'owner', 'group', 'priority', 'body')
        extra_kwargs = {'owner': {'write_only': True}}


class AppealSerializer(serializers.ModelSerializer):
    body = serializers.CharField(source='html_body', read_only=True, label='Текст Обращения')

    class Meta:
        model = Appeal
        fields = ('id', 'title', 'auditorium', 'status', 'group', 'priority', 'body')
