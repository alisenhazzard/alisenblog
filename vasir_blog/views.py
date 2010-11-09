"""==========================================================================
views_base_pages.py

Handles various page renders 
============================================================================="""
#Import everything from the views_util
from vasir_site.views_util import *
#Import models
import models

#python imports
#----------------------------------------
import math

#Import admin to register models
from django.contrib import admin
"""=============================================================================

Functions

============================================================================="""
@render_to('vasir_blog/blog.html')
def blog(request, **kwargs):
    '''blog(request, **kwargs)
    -------------------------------------
    Handles grabbing blog posts by date / category / tag '''
    #------------------------------------
    #
    #Data to get based on request
    #
    #------------------------------------
    #------------------------------------
    #See if a single page was requested
    #------------------------------------
    try:
        if kwargs['query_type'] == 'single':
            return get_single_post(request, kwargs)
    except KeyError:
        #They didn't request a single post, so continue on
        pass
    
    #------------------------------------
    #PAGINATION PRE-SETUP
    #------------------------------------
    #Get posts per page
    try:
        if kwargs['posts_per_page']:
            kwargs['posts_per_page'] = int(kwargs['posts_per_page'])
    except KeyError:
        #If none is passed in, use 5
        kwargs['posts_per_page'] = 5

    #Get current page
    try:
        if kwargs['current_page']:
            kwargs['current_page'] = int(kwargs['current_page'])
    except KeyError:
        #If none is passed in, use 10
        kwargs['current_page'] = 1
    
    #------------------------------------
    #QUERY SET UP
    #------------------------------------
    
    #Get filter type
    #------------------------------------
    try:
        if kwargs['filter_type']:
            pass
    except KeyError:
        #If none is passed in, assume 'slug'
        kwargs['filter_type'] = None

    #Get filter col
    #------------------------------------
    try:
        if kwargs['filter_col']:
            pass
    except KeyError:
        #If none is passed in, assume 'slug'
        kwargs['filter_col'] = 'name'

    #Get filter value
    #------------------------------------
    try:
        if kwargs['filter_value']:
            pass
    except KeyError:
        #If none is passed in, assume 'slug'
        kwargs['filter_value'] = ''

    #------------------------------------
    #GET POSTS
    #------------------------------------
    #Get posts based on passed in kwargs
    #Build dict to unpack
    if kwargs['filter_type'] is not None:
        #if they didn't pass in a filter_type, it means we should show
        #   all blog posts
        filter_dict = {'%s__%s__contains' % (
            kwargs['filter_type'],
            kwargs['filter_col']): 
                kwargs['filter_value']
        }

        #Grab the posts that match the filter
        #   (e.g., get posts that belong to a passed in category)
        #unpack the filter dict we just created above so we can use
        #   variable column names
        total_posts = models.Post.objects.filter(
            **filter_dict).count()
        
        #Get the total number of pages
        total_pages = math.ceil(
            float(total_posts) / kwargs['posts_per_page'])
    
        #Get the posts
        posts = models.Post.objects.filter(
            **filter_dict)[
            ((kwargs['current_page'] - 1) * kwargs['posts_per_page']):
            (kwargs['current_page'] * kwargs['posts_per_page'])
        ]

    elif kwargs['filter_type'] is None:
        #Get the number of posts
        total_posts = models.Post.objects.count()

        #Get the total number of pages
        total_pages = math.ceil(
            float(total_posts) / kwargs['posts_per_page'])
    
        #Get the posts
        posts = models.Post.objects.all()[
            ((kwargs['current_page'] - 1) * kwargs['posts_per_page']):
            (kwargs['current_page'] * kwargs['posts_per_page'])
        ]

    #------------------------------------
    #More Pagination Stuff
    #------------------------------------
    previous_page = None
    if kwargs['current_page'] > 1:
        previous_page = kwargs['current_page'] - 1

    next_page= None
    if kwargs['current_page'] < total_pages: 
        next_page = kwargs['current_page'] + 1

    #------------------------------------
    #
    #Data to get for all pages
    #
    #------------------------------------
    #We need to get the 5 latest posts for the sidebas
    latest_posts = get_latest_posts()

    #Get all the categories
    all_categories = get_all_categories()

    #Finally, return everything
    return {
        'latest_posts': latest_posts,
        'all_categories': all_categories,
        
        'posts': posts,

        'filter_type': kwargs['filter_type'],
        'filter_value': kwargs['filter_value'],

        'current_page': kwargs['current_page'],
        'posts_per_page': kwargs['posts_per_page'],
        'total_posts': int(total_posts),
        'total_pages': int(total_pages),

        'previous_page': previous_page,
        'next_page': next_page,
    }



#----------------------------------------
#Get the latest posts to show across all parts of the blog
#----------------------------------------
def get_latest_posts():
    latest_posts = models.Post.objects.order_by('-post_date')[:5]
    return latest_posts

#----------------------------------------
#Get all the categories
#----------------------------------------
def get_all_categories():
    all_categories = models.Category.objects.all().order_by('name')
    return all_categories


#----------------------------------------
#Get a single post
#----------------------------------------
@render_to('vasir_blog/post_single.html')
def get_single_post(request, kwargs):
    #Get single post 
    post_object = models.Post.objects.get(
        slug=kwargs['filter_value'])
   
    #We need to get the 5 latest posts for the sidebas
    latest_posts = get_latest_posts()

    #Get all the categories
    all_categories = get_all_categories()

    return {
        'latest_posts': latest_posts,
        'all_categories': all_categories,
        'post': post_object,
    }

"""=============================================================================

Admin site registration

============================================================================="""
#Register mode
admin.site.register(models.Category)
#Register model
admin.site.register(models.Tag)
#Register model
admin.site.register(models.Post)
