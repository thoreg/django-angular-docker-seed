from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view

from apps.sampleapp.views import index as index_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-doc/$', schema_view),
    url(r'^api/', include('apps.sampleapp.urls')),


    url(r'^$', index_view, name='index'),
    url(r'^.*', index_view) #catch-all
]
