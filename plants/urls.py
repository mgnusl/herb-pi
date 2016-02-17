from django.conf.urls import url
from plants import views

urlpatterns = [
 	url(r'^plants/$', views.plant_list),
    url(r'^plant/(?P<pk>[0-9]+)/$', views.plant_detail),
]