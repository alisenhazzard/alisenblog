from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #===========================================================================
    #
    #   Site Wide Pages
    #
    #===========================================================================
    url(r'^$',
        'site.views.home',
        name='page_home'),
    
    url(r'openlayers_book/$',
        'site.views.openlayers_book',
        name='page_openlayers_book'),

    url(r'openlayers_book/files/$',
        'site.views.openlayers_book',
        name='page_openlayers_book'),

    url(r'^about/$',
        'site.views.about',
        name='page_about'),
    
    url(r'^dev/$',
        'site.views.dev',
        name='page_dev'),

    url(r'^portfolio/$',
        'site.views.portfolio',
        name='page_portfolio'),
)
