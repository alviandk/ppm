from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.EditView.as_view(), name='edit'),
    url(r'^add/$', views.AddView.as_view(), name='add'),
)
