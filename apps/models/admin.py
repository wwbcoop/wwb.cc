# Import django packages
from django.contrib import admin
from django.contrib.contenttypes import admin as generic
from django.urls import reverse
from django.utils.html import format_html
from django.db.models.fields import BLANK_CHOICE_DASH

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
    ordering = ("object_id",)
    thumb = AdminThumbnail(image_field=cached_admin_thumb)

    def get_action_choices(self, request):
        """
        Override blank action string
        @see https://stackoverflow.com/questions/35503403/how-to-remove-in-django-admin-action
        """
        return super(ImageAdmin, self).get_action_choices(request, [("", "Elige una acción")])

# Image inlines

class ImageInline(generic.GenericTabularInline):
    model  = models.Image
    extra  = 1
    list_display = ('thumb', 'content_object', 'alt_text', 'move')
    sortable_field_name = "position"

    def move(self, obj):
        return format_html(
            '<span>⤮</span>'
        )

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

def cached_project_thumb(instance):
    cached = ImageCacheFile(AdminThumbnailSpec(instance.images.first().image_file))
    cached.generate()
    return cached

class ProjectAdmin(admin.ModelAdmin):
    model = models.Project
    ordering = ('name',)
    inlines = [
        ImageInline,
    ]
    list_display = ('name', 'thumb', 'category', 'end_date', 'published', 'featured', 'ver')
    list_filter  = ('published', 'featured', 'category')
    actions      = [publish, unpublish, unfeature, feature]
    thumb        = AdminThumbnail(image_field=cached_project_thumb)

    def get_action_choices(self, request):
        """
        Override blank action string
        @see https://stackoverflow.com/questions/35503403/how-to-remove-in-django-admin-action
        """
        return super(ProjectAdmin, self).get_action_choices(request, [("", "Elige una acción")])


    class Media:
        js = (
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',
            '/static/wwb/js/menu-sort.js',
        )


    def ver(self, obj):
        return format_html(
            '<a href="{}" target="_blank">Ver {}</a>',
            reverse('project', kwargs={'slug': obj.slug}),
            obj.name,
        )

class RelatedEntityAdmin(admin.ModelAdmin):
    model = models.RelatedEntity
    ordering = ('name',)
    list_display = ('name', 'link')

    def get_action_choices(self, request):
        """
        Override blank action string
        @see https://stackoverflow.com/questions/35503403/how-to-remove-in-django-admin-action
        """
        return super(RelatedEntityAdmin, self).get_action_choices(request, [("", "Elige una acción")])

class TechTaxonomyAdmin(admin.ModelAdmin):
    model = models.TechTaxonomy
    ordering = ('name',)
    list_display = ('name', 'description')

    def get_action_choices(self, request):
        """
        Override blank action string
        @see https://stackoverflow.com/questions/35503403/how-to-remove-in-django-admin-action
        """
        return super(TechTaxonomyAdmin, self).get_action_choices(request, [("", "Elige una acción")])

class LinkAdmin(admin.ModelAdmin):
    model = models.TechTaxonomy
    ordering = ('name',)
    list_display = ('name', 'link')

    def get_action_choices(self, request):
        """
        Override blank action string
        @see https://stackoverflow.com/questions/35503403/how-to-remove-in-django-admin-action
        """
        return super(LinkAdmin, self).get_action_choices(request, [("", "Elige una acción")])



admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.RelatedEntity, RelatedEntityAdmin)
admin.site.register(models.TechTaxonomy, TechTaxonomyAdmin)
