from django.conf.urls import url
from plants import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^plants/$', views.plant_list),
    url(r'^plant/(?P<pk>[0-9]+)/$', views.plant),
    url(r'^moisturelog/(?P<fk>[0-9]+)/$', views.moisture_sensor_log),
    url(r'^wateringlog/(?P<fk>[0-9]+)/$', views.watering_log),
    url(r'^plantinstance/(?P<pk>[0-9]+)/$', views.plant_instance),
    url(r'^plantinstances/$', views.plantinstance_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
