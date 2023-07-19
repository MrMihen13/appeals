from rest_framework import serializers

from core.models import Appeal


class CreateAppealSerializer(serializers.ModelSerializer):
    body = serializers.CharField(source='markdown_body', write_only=True)

    class Meta:
        model = Appeal
        fields = ('title', 'group', 'priority', 'body')


class AppealSerializer(serializers.ModelSerializer):
    body = serializers.CharField(source='html_body', read_only=True)

    class Meta:
        model = Appeal
        fields = ('id', 'title', 'status', 'group', 'priority', 'body')
