from django.conf.urls import url

from lasotuvi_django.views import api, lasotuvi_django_index

urlpatterns = [
    url(r'^api', api),
    url(r'^$', lasotuvi_django_index)
]