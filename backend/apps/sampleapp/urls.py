from django.conf.urls import url, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'v1/tasks', views.TaskListViewSet)
router.register(r'v1/frontusers', views.FrontUserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
