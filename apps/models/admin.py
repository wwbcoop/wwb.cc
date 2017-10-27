# Import django packages
from django.contrib import admin

# Import project packages
from . import models

admin.site.register(models.Image)
admin.site.register(models.Project)
admin.site.register(models.Client)
admin.site.register(models.TechTaxonomy)
