from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "about/about.html"}, name="about"),
    
    url(r'^privacy/$', direct_to_template, {"template": "about/privacy.html"}, name="privacy"),
    
    url(r'^what_next/$', direct_to_template, {"template": "about/what_next.html"}, name="what_next"),
)
