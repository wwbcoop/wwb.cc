# Import python packages
import time
import datetime

# Import contrib packages
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# import project packages
from .validators import ImageTypeValidator, ImageSizeValidator

# Bound methods moved from model to avoid problems with serialization in migrations
validate_image_size  = ImageSizeValidator({ 'min_width' : 600, 'min_height' : 300, 'max_width' : 1920, 'max_height' : 1280 })
validate_image_type  = ImageTypeValidator(["jpeg", "png"])


class Image(models.Model):
    """A model container for image fields."""

    image_file = models.ImageField(_("Archivo"), blank=False,
                                    validators = [validate_image_size, validate_image_type],
                                    help_text=_("Sube una imagen representativa haciendo click en la imagen inferior."
                                                "La imagen ha de tener ancho mínimo de 300 píxeles y máximo de 1920, y altura mínima "
                                                "de 300 píxeles y máxima de 1280. Formatos permitidos: PNG, JPG, JPEG."))
    alt_text   = models.CharField(_("Texto alternativo"), max_length=128,
                 help_text=_("Texto que describe la imagen para screen readers "))
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id      = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        """String representation of model instances"""
        return self.alt_text


class Project(models.Model):
    """Projects of wwb.cc"""

    name          = models.CharField(_("Nombre del proyecto"), max_length=128, unique=True,
                    help_text=_("El nombre del proyecto"))
    slug          = models.SlugField(editable=False, blank=True)
    creation_date = models.DateField(editable=False, blank=True, null=True)
    update_date   = models.DateField(editable=False, blank=True, null=True)
    summary       = models.TextField(_("Resumen"), blank=True,
                    help_text=_("Una resumen corto del proyecto para cabeceras y vistas."))
    start_date    = models.DateField(_("Fecha de comienzo"), editable=False, blank=True, null=True,
                    help_text=_("Fecha aproximada de comienzo del proyecto."))
    end_date      = models.DateField(_("Fecha de finalización"), editable=False, blank=True, null=True,
                    help_text=_("Fecha aproximada de finalización del proyecto."))

    def __str__(self):
        """String representation of model instances"""
        return self.name

    def save(self, *args, **kwargs):
        """Custom save functions that populates automatically 'slug' and 'creation_date' fields"""
        self.slug = slugify(self.name)
        self.update_date = datetime.datetime.now()
        # Set creation date only when node is saved and hasn't an ID yet, therefore
        if not self.id:
            self.creation_date = datetime.datetime.now()
        super(Project, self).save(*args, **kwargs)
