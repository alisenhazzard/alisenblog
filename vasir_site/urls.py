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
    
    url(r'openlayers_book/$',
        'vasir_site.views.openlayers_book',
        name='page_openlayers_book'),

    url(r'openlayers_book/files/$',
        'vasir_site.views.openlayers_book',
        name='page_openlayers_book'),

    url(r'^about/$',
        'vasir_site.views.about',
        name='page_about'),
    
    url(r'^dev/$',
        'vasir_site.views.dev',
        name='page_dev'),

    url(r'^portfolio/$',
        'vasir_site.views.portfolio',
        name='page_portfolio'),
)
