from django.conf.urls import url
from plants import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^plants/$', views.plant_list),
    url(r'^sensorlog/$', views.sensor_log),
    url(r'^plant/(?P<pk>[0-9]+)/$', views.plant_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
