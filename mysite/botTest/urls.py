from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ryo$', views.index, name='index'),
    url(r'^ryo\/ajax$', views.ajaxFunc, name='ajaxFunc'),
    url(r'^saki$', views.index, name='indexS'),
    url(r'^saki\/ajax$', views.ajaxFunc, name='ajaxFuncS'),
]
