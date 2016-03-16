from django.conf.urls import url
from plants import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^plants/$', views.plant_list),
    url(r'^plant/(?P<pk>[0-9]+)/$', views.plant_detail),
    url(r'^sensorlog/$', views.moisture_sensor_log),
    url(r'^wateringlog/$', views.watering_log),
    url(r'^plantinstance/$', views.plant_instance),
]

urlpatterns = format_suffix_patterns(urlpatterns)
