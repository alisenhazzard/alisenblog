"""==========================================================================
views_base_pages.py

Handles various page renders 
============================================================================="""
#Import everything from the views_util
from views_util import *

"""=============================================================================

Functions

============================================================================="""
"""--------------------------------------
home: renders the home page
-----------------------------------------"""
@cache_page(60 * 30 * 3)
@render_to('vasir_site/home.html')
def home(request):
    #Get the latest post
    latest_post = blog_models.Post.objects.order_by('-post_date')[0]
    return {
        'latest_post': latest_post
    }

"""--------------------------------------
openlayers_book: renders the home page
-----------------------------------------"""
@cache_page(60 * 60 * 3)
@render_to('vasir_site/openlayers_book.html')
def openlayers_book(request):
    #Get the latest post
    return {}

'''OpenLayers Book Files.  Contains source code and other files 
    for the book'''
@cache_page(60 * 60 * 3)
@render_to('vasir_site/openlayers_book_files.html')
def openlayers_book_files(request):
    #Get the latest post
    return {}

"""--------------------------------------
about: renders the home page
-----------------------------------------"""
@cache_page(60 * 60 * 3)
@render_to('vasir_site/about.html')
def about(request):
    return {}


"""--------------------------------------
portfolio: renders the home page
-----------------------------------------"""
@cache_page(60 * 60 * 3)
@render_to('vasir_site/portfolio.html')
def portfolio(request):
    return {}

"""--------------------------------------
dev: renders the home page
-----------------------------------------"""
@cache_page(60 * 60 * 3)
@render_to('vasir_site/dev.html')
def dev(request):
    return {}
