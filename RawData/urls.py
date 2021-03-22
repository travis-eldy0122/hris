from django.conf.urls import include, url
from . import views

app_name = 'RawData'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thankyou$', views.thankyou, name='thankyou'),
    url(r'^school_request', views.school_request, name='school_request'),
    url(r'^position_request', views.position_request, name='position_request'),
    url(r'^addstaff_request', views.addstaff_request, name='addstaff_request'),
]