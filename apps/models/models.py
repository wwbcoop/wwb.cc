# python
import time, datetime

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now

# contrib
from ckeditor_uploader.fields import RichTextUploadingField

# project
from .validators import ImageTypeValidator, ImageSizeValidator
from .utils import RenameProjectImage
from . import categories

# Bound methods moved from model to avoid problems with serialization in migrations
validate_image_size = ImageSizeValidator({ 'min_width' : 600, 'min_height' : 300, 'max_width' : 1920, 'max_height' : 1280 })
validate_image_type = ImageTypeValidator(["jpeg", "png"])
project_images_path = RenameProjectImage()


class RelatedEntity(models.Model):
    """A model container for clients."""

    name     = models.CharField(_("Nombre de la entidad"), max_length=128, blank=False)
    link     = models.URLField(_("Enlace a un site relacionado"), help_text=_("Enlace opcional para obtener más info sobre el cliente") )
    category = models.URLField(_("Categoría"), choices=categories.ENTITY_CATEGORIES,
               help_text=_("Especifica la relación de la entidad con el proyecto") )

    def __str__(self):
        """String representation of model instances"""
        return self.name


class TechTaxonomy(models.Model):
    """A model container for clients."""

    name        = models.CharField(_("Tecnología"), max_length=128, blank=False,
                                   help_text=_("Nombre de la tecnología"))
    description = models.TextField(_("Resumen"), blank=True,
                                   help_text=_("Una resumen corto de la tecnología."))

    def __str__(self):
        """String representation of model instances"""
        return self.name


class Image(models.Model):
    """A model container for image fields."""

    image_file     = models.ImageField(_("Archivo"), blank=False, upload_to = project_images_path,
                                       validators = [validate_image_size, validate_image_type],
                                       help_text=_("Sube una imagen representativa haciendo click en la imagen inferior."
                                                   "La imagen ha de tener ancho mínimo de 300 píxeles y máximo de 1920, y altura mínima "
                                                   "de 300 píxeles y máxima de 1280. Formatos permitidos: PNG, JPG, JPEG."))
    alt_text       = models.CharField(_("Texto alternativo"), max_length=128, blank=False,
                     help_text=_("Texto que describe la imagen para screen readers "))
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id      = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        """String representation of model instances"""
        return self.image_file.name


class Project(models.Model):
    """Projects of wwb.cc"""

    name           = models.CharField(_("Nombre del proyecto"), max_length=128, unique=True,
                     help_text=_("El nombre del proyecto"))
    slug           = models.SlugField(_("Slug"), editable=False, blank=False)
    category       = models.CharField(_("Categoría"), max_length=128, choices=categories.PROJECT_CATEGORIES, blank=False, default='DI',
                     help_text=_("Categoría del proyecto"))
    published_date = models.DateField(_("Fecha de publicación"), blank=False, null=True, default=now)
    summary        = models.TextField(_("Resumen"), blank=True,
                     help_text=_("Una resumen corto del proyecto para cabeceras y vistas."))
    body           = RichTextUploadingField(_("Descripción del proyecto"), blank=True)
    start_date     = models.DateField(_("Fecha de comienzo"), blank=True, null=True,
                     help_text=_("Fecha aproximada de comienzo del proyecto."))
    end_date       = models.DateField(_("Fecha de finalización"), blank=True, null=True,
                     help_text=_("Fecha aproximada de finalización del proyecto."))
    related_entity = models.ManyToManyField(RelatedEntity, verbose_name=_("Entidades relacionadas"), blank=True,
                     help_text=_("Especifica aquí los clientes del Proyecto."))
    technology     = models.ManyToManyField(TechTaxonomy, verbose_name=_("Tecnologías empleadas"), blank=True,
                     help_text=_("Especifica aquí tecnologías empleadas en el Proyecto."))
    published      = models.BooleanField(_("Publicado"), blank=False, default=False)
    featured       = models.BooleanField(_("Destacado"), blank=False, default=False)

    def __str__(self):
        """String representation of model instances"""
        return self.name

    def save(self, *args, **kwargs):
        """Custom save functions that populates automatically 'slug' and 'creation_date' fields"""
        self.update_date = now
        self.slug = slugify(self.name)
        # Set creation date only when node is saved and hasn't an ID yet, therefore
        if not self.id:
            self.creation_date = now
        super(Project, self).save(*args, **kwargs)
