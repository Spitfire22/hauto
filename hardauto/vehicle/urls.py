from django.conf.urls import url
from . import views

app_name = 'vehicle'
urlpatterns = [
    url(r'^$', views.vehicle_list, name='vehicle_list'),
    url(r'^choicebar/$', views.choicebar, name='choicebar'),
    url(r'^getmodels/$', views.getmodels, name='getmodels')
]