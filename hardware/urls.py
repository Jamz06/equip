from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^region/([0-9]+)/$', views.Toch_dost_View.as_view(), name='toch_dost'),
    
    url(r'^overview/', views.overview, name='overview'),
    
]
