from django.conf.urls.defaults import *
import models

urlpatterns = patterns('',
    #===========================================================================
    #
    #  Blog Pages 
    #
    #===========================================================================
    #Root blog page
    url(r'^$',
        'vasir_blog.views.blog',
        name='blog',
        ),
    
    #Specific blog page
    url(r'^page/(?P<current_page>\d{1,3})/$',
        'vasir_blog.views.blog',
        ),

    #Get a single blog post
    url(r'^(?P<category>[^/]+)/(?P<filter_value>[^/]+)/$',
        'vasir_blog.views.blog',
        {
        'query_type': 'single',
        }),

    #===========================================================================
    #   CATEGORIES 
    #===========================================================================
    #Get posts by category
    url(r'^(?P<filter_value>[^/]+)/$',
        'vasir_blog.views.blog',
        {'model': models.Category,
        'filter_type': 'category',
        'filter_col': 'slug',
        }),

    #===========================================================================
    #   TAGS
    #===========================================================================
    #Get a list of blog posts by tag
    url(r'^tags/(?P<filter_value>[^/]+)/$',
        'vasir_blog.views.blog',
        {'model': models.Tag,
        'filter_type': 'tag',
        'filter_col': 'slug',
        }),
)
