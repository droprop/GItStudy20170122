from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ryo$', views.index, name='index'),
    url(r'^ryo/ajax$', views.ajaxFunc, name='ajaxFunc'),
]
