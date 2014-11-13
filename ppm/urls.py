from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^items/', include('inventory.urls', namespace="items")),
    url(r'^admin/', include(admin.site.urls)),
)
