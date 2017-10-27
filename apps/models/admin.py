# Import django packages
from django.contrib import admin
from django.contrib.contenttypes import admin as generic

# Import project packages
from . import models


class ImageInline(generic.GenericTabularInline):
    model  = models.Image
    extra  = 1

class ProjectAdmin(admin.ModelAdmin):
    model = models.Project
    inlines = [
        ImageInline,
    ]

admin.site.register(models.Image)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.RelatedEntity)
admin.site.register(models.TechTaxonomy)
