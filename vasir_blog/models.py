"""==========================================================================
models.py

Contains all our models for the blog app 

============================================================================="""
from django.db import models
from django.conf import settings

"""=============================================================================

Models

============================================================================="""
#----------------------------------------
#Category 
#----------------------------------------
class Category(models.Model):
    #slug is the 'short' version of the category, used for URLs and the PK
    slug = models.CharField(
        primary_key=True,
        max_length=255
    )
    #name of the category post
    name = models.CharField(
        max_length=255
    )

    #description is a short description of the object
    description = models.TextField()

    #------------------------------------
    #Category functions
    #------------------------------------
    def get_post_count(self):
        #Return the URL as category/post
        return self.post_set.count()
    def get_url(self):
        #Return the URL as category/post
        return '/blog/%s/' % (
            self.slug)

    def __unicode__(self):
        return self.name

#----------------------------------------
#Tags
#----------------------------------------
class Tag(models.Model):
    #slug is the 'short' version of the tag name, used for URLs and the PK
    slug = models.CharField(
        primary_key=True,
        max_length=255
    )

    #name is what the tag is called
    name = models.CharField(
        max_length=255
    )

    #description is a short description of the object
    description = models.TextField()

    #------------------------------------
    #Tag functions
    #------------------------------------
    def get_url(self):
        #Return the URL as category/post
        return '/blog/tags/%s/' % (
            self.slug)

    def __unicode__(self):
        return self.name

#----------------------------------------
#Post 
#----------------------------------------
class Post(models.Model):
    #Slug is the 'short' version of the title, used in the URL and
    #   used as the primary key
    slug = models.CharField(
        primary_key=True,
        max_length=255
    )

    #title of blog post
    title = models.CharField(
        max_length=255
    )

    #Save the post date
    post_date = models.DateTimeField()

    #If the post has been edited
    post_last_edit_date = models.DateTimeField(
        blank=True,
        null=True
    )

    #num_views will store the times the page has been accessed
    num_views = models.IntegerField(
        blank=True, 
        null=True
    )

    #optional image
    related_image = models.ImageField(
        'Associated Image',
        blank=True,
        null=True,
        upload_to='blog_images'
    )

    #category the post belongs to
    category = models.ForeignKey(Category)

    #tags this post contains
    tags = models.ManyToManyField(
        Tag, 
        null=True, 
        blank=True)

    #content is the actual contents of the post
    content = models.TextField()

    #Short description of the post
    description = models.TextField()

    #------------------------------------
    #Post functions
    #------------------------------------
    def get_url(self):
        #Return the URL as category/post
        return '/blog/%s/%s/' % (
            self.category.slug,
            self.slug)

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.slug)
