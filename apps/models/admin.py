# Import django packages
from django.contrib import admin

# Import project packages
from . import models

admin.site.register(models.Image)
admin.site.register(models.Project)
