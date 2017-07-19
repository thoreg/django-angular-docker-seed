from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('id', 'slug', 'text', 'created_at', 'updated_at')
        model = Task
        read_only_fields = ('id', 'slug')
