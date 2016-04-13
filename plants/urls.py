from django.conf.urls import url
from plants import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^api/plants/$', views.plant_list),
    url(r'^api/plant/(?P<pk>[0-9]+)/$', views.plant),
    url(r'^api/moisturelog/(?P<fk>[0-9]+)/$', views.moisture_sensor_log),
    url(r'^api/wateringlog/(?P<fk>[0-9]+)/$', views.watering_log),
    url(r'^api/plantinstance/(?P<pk>[0-9]+)/$', views.plant_instance),
    url(r'^api/plantinstances/$', views.plantinstance_list),
    url(r'^plants/$', views.plants_index, name='plants/index'),
    url(r'^instances/$', views.plant_instances_index, name='instances/index'),
    url(r'^instances/new/$', views.new_plant_instance, name='instances/new'),
    url(r'^instances/edit/(?P<id>\w+)$', views.new_plant_instance, name='instances/edit'),
    url(r'^instances/calibrate/(?P<plant_instance_id>\w+)$', views.calibrate_sensor, name='calibrate'),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
