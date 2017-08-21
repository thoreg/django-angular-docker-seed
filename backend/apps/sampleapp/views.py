from django.shortcuts import render
from .models import Task, FrontUser
from .serializers import TaskSerializer, FrontUserSerializer

from rest_framework import viewsets as drf_viewsets
from rest_framework_mongoengine import viewsets


class FrontUserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = FrontUserSerializer

    def get_queryset(self):
        return FrontUser.objects.all()







#
# Begin original seed project
#

class TaskListViewSet(drf_viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Create your views here.
def index(request):
    return render(request, "sampleapp/index.html")
