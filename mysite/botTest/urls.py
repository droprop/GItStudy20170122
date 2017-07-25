from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ryo$', views.index, name='index'),
    url(r'^ryo\/ajax$', views.ajaxFunc, name='ajaxFunc'),
    url(r'^saki$', views.indexS, name='indexS'),
    url(r'^saki\/ajax$', views.ajaxFuncS, name='ajaxFuncS'),
]
