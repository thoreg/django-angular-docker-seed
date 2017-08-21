from rest_framework import serializers as drf_serializers
from rest_framework_mongoengine import serializers
from .models import Task, FrontUser


class FrontUserSerializer(serializers.DocumentSerializer):
    class Meta:
        fields = '__all__'
        model = FrontUser


#
# Begin old example models from the original project
#


class TaskSerializer(drf_serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('id', 'slug', 'text', 'created_at', 'updated_at')
        model = Task
        read_only_fields = ('id', 'slug')
