# Import python packages
import time
from datetime import date

# Import packages
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

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
        self.update_date = now
        # Set creation date only when node is saved and hasn't an ID yet, therefore
        if not self.id:
            self.creation_date = now
        super(Project, self).save(*args, **kwargs)
