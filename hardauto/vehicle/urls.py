from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.vehicle_list, name="vehicle_list"),
    url(r'^choicebar/$', views.choicebar, name="choicebar")
]