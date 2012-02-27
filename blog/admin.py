from blog import models
from django.contrib import admin

admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Post)
