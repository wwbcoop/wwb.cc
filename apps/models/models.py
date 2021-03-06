# python
import time, datetime

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
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


class Link(models.Model):
    """A model container for clients."""

    name     = models.CharField(_("Nombre del sitio"), max_length=128, blank=False)
    link     = models.URLField(_("Enlace al site"))
    summary  = models.TextField(_("Resumen"), blank=True,
               help_text=_("Una resumen corto opcional del contenido."))

    def __str__(self):
        """String representation of model instances"""
        return self.name

    class Meta:
        verbose_name        = _('Enlace')
        verbose_name_plural = _('Enlaces')

class RelatedEntity(models.Model):
    """A model container for clients."""

    name     = models.CharField(_("Nombre de la entidad"), max_length=128, blank=False)
    link     = models.URLField(_("Enlace a un site relacionado"), help_text=_("Enlace opcional para obtener más info sobre el cliente") )

    def __str__(self):
        """String representation of model instances"""
        return self.name

    class Meta:
        verbose_name        = _('Entidad relacionada')
        verbose_name_plural = _('Entidades relacionadas')

class TechTaxonomy(models.Model):
    """A model container for clients."""

    name        = models.CharField(_("Tecnología"), max_length=128, blank=False,
                                   help_text=_("Nombre de la tecnología"))
    description = models.TextField(_("Resumen"), blank=True,
                                   help_text=_("Una resumen corto de la tecnología."))

    def __str__(self):
        """String representation of model instances"""
        return self.name

    class Meta:
        verbose_name        = _('Tecnología')
        verbose_name_plural = _('Tecnologías')


class Image(models.Model):
    """A model container for image fields."""

    image_file     = models.ImageField(_("Archivo"), blank=False, upload_to = project_images_path,
                                       validators = [validate_image_size, validate_image_type],
                                       help_text=_("Sube una imagen representativa haciendo click en la imagen inferior."
                                                   "La imagen ha de tener ancho mínimo de 300 píxeles y máximo de 1920, y altura mínima "
                                                   "de 300 píxeles y máxima de 1280. Formatos permitidos: PNG, JPG, JPEG."))
    alt_text       = models.CharField(_("Texto alternativo"), max_length=128, blank=False,
                     help_text=_("Texto que describe la imagen para screen readers "))
    credits        = models.CharField(_("Créditos"), max_length=128, blank=True,
                     help_text=_("Especifica los créditos de la imagen en caso necesario"))
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id      = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    position       = models.PositiveSmallIntegerField("Position", null=True)

    def __str__(self):
        """String representation of model instances"""
        return self.image_file.name

    class Meta:
        verbose_name        = _('Imagen')
        verbose_name_plural = _('Imágenes')
        ordering = ['position']

class Project(models.Model):
    """Projects of wwb.cc"""

    name           = models.CharField(_("Nombre del proyecto"), max_length=128, unique=True,
                     help_text=_("El nombre del proyecto"))
    slug           = models.SlugField(_("Slug"), editable=False, blank=False)
    category       = models.CharField(_("Categoría"), max_length=128, choices=categories.PROJECT_CATEGORIES, blank=False, default='DI',
                     help_text=_("Categoría del proyecto"))
    summary        = models.TextField(_("Resumen"), blank=True,
                     help_text=_("Una resumen corto del proyecto para cabeceras y vistas."))
    body           = RichTextUploadingField(_("Descripción del proyecto"), blank=True,
                     help_text=_("Descripción del proyecto."))
    images         = GenericRelation(Image, related_query_name='projects')
    start_date     = models.DateField(_("Fecha de comienzo"), blank=True, null=True,
                     help_text=_("Fecha aproximada de comienzo del proyecto. Usa el datepicker o el formato dd/mm/yyyy."))
    end_date       = models.DateField(_("Fecha de finalización"), blank=True, null=True,
                     help_text=_("Fecha aproximada de finalización del proyecto. Usa el datepicker o el formato dd/mm/yyyy."))
    clients        = models.ManyToManyField(RelatedEntity, related_name='clients', verbose_name=_("Clientes"), blank=True,
                     help_text=_("Indica clientes del proyecto. Puedes añadir nuevos clicando en el +"))
    collaborators  = models.ManyToManyField(RelatedEntity, related_name='collaborators', verbose_name=_("Colaborador@s"), blank=True,
                     help_text=_("Indica colaboradores del proyecto. Puedes añadir nuevos clicando en el +"))
    technology     = models.ManyToManyField(TechTaxonomy, verbose_name=_("Tecnologías empleadas"), blank=True,
                     help_text=_("Especifica aquí tecnologías empleadas en el Proyecto."))
    links          = models.ManyToManyField(Link, verbose_name=_("Enlaces"), blank=True,
                     help_text=_("Especifica aquí enlaces para ampliar información del proyecto."))
    related        = models.ManyToManyField('models.Project', verbose_name=_("Proyectos relacionados"), blank=True,
                     help_text=_("Otros proyectos relacionados con éste."))
    published      = models.BooleanField(_("Publicado"), blank=False, default=False)
    featured       = models.BooleanField(_("Destacado"), blank=False, default=False)


    def __str__(self):
        """String representation of model instances"""
        return self.name

    def save(self, *args, **kwargs):
        """Custom save functions that populates automatically 'slug' and 'creation_date' fields"""
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name        = _('Proyecto')
        verbose_name_plural = _('Proyectos')
