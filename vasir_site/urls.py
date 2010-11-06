from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #===========================================================================
    #
    #   Site Wide Pages
    #
    #===========================================================================
    url(r'^$',
        'vasir_site.views.home',
        name='page_home'),
)
