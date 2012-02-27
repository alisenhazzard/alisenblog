"""==========================================================================
views_util.py

Contains various utility-type functions to be used across views

============================================================================="""
#python imports
#========================================
import re
import datetime
import random
import json
import hashlib

#django imports
#========================================
from django.shortcuts import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.core.mail import EmailMessage, SMTPConnection, send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_page

import django.db.models
from django.conf import settings

#site app imports
#========================================
import blog.models as blog_models

"""==========================================================================

Util Functions

============================================================================="""
#----------------------------------------
#context processor
#----------------------------------------
#If we want to use an additional context processor, here's a template for it
def additional_context_processor(request):
    return {'key': 'value'}

#----------------------------------------
#wraps function
#----------------------------------------
try:
    from functools import wraps
except ImportError: 
    def wraps(wrapped, assigned=('__module__', '__name__', '__doc__'),
              updated=('__dict__',)):
        def inner(wrapper):
            for attr in assigned:
                setattr(wrapper, attr, getattr(wrapped, attr))
            for attr in updated:
                getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
            return wrapper
        return inner

#----------------------------------------
#render_to for template rendering
#----------------------------------------
def render_to(template=None, mimetype="text/html"):
    def renderer(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            output = function(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output
            tmpl = output.pop('TEMPLATE', template)
            return render_to_response(tmpl, 
                output,
                context_instance=RequestContext(request),
                mimetype=mimetype)
        return wrapper
    return renderer
