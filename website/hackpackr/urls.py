from django.conf.urls import include, patterns, url

from hackpackr import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)