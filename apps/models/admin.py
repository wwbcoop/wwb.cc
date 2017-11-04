# Import django packages
from django.contrib import admin
from django.contrib.contenttypes import admin as generic
from django.urls import reverse
from django.utils.html import format_html

# contrib
from imagekit import ImageSpec
from imagekit.admin import AdminThumbnail
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile

# Import project packages
from . import models

# Thumbnail generator for admin views
# @see https://github.com/matthewwithanm/django-imagekit#user-content-admin

class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(100, 100)]
    format = 'JPEG'
    options = {'quality': 90 }

def cached_admin_thumb(instance):
    cached = ImageCacheFile(AdminThumbnailSpec(instance.image_file))
    cached.generate()
    return cached

class ImageAdmin(admin.ModelAdmin):
    model = models.Image
    list_display = ('thumb', 'content_object', 'alt_text')
    thumb = AdminThumbnail(image_field=cached_admin_thumb)

# Image inlines

class ImageInline(generic.GenericTabularInline):
    model  = models.Image
    extra  = 1
    sortable_field_name = "position"

# Project admin

def publish(modeladmin, request, queryset):
    queryset.update(published=True)

publish.short_description = "Publica los proyectos seleccionados"

def unpublish(modeladmin, request, queryset):
    queryset.update(published=False)

unpublish.short_description = "Despublica los proyectos seleccionados"

def feature(modeladmin, request, queryset):
    queryset.update(featured=True)

feature.short_description = "Promociona los proyectos seleccionados"

def unfeature(modeladmin, request, queryset):
    queryset.update(featured=False)

unfeature.short_description = "Retira la promoción de los proyectos seleccionados"

class ProjectAdmin(admin.ModelAdmin):
    model = models.Project
    ordering = ('name',)
    inlines = [
        ImageInline,
    ]
    list_display = ('name', 'category', 'end_date', 'published', 'featured', 'ver')
    list_filter  = ('published', 'featured', 'category')
    actions = [publish, unpublish, unfeature, feature]

    def ver(self, obj):
        return format_html(
            '<a href="{}" target="_blank">Ver {}</a>',
            reverse('project', kwargs={'slug': obj.slug}),
            obj.name,
        )



# Register everything

admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Link)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.RelatedEntity)
admin.site.register(models.TechTaxonomy)
