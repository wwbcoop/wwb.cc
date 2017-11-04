from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill, ResizeToFit, ResizeToCover

"""
Image generators to be used by models
@see https://pypi.python.org/pypi/django-imagekit#using-specs-in-templates
"""

class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 100)]
    format = 'JPEG'
    options = { 'quality' : 90 }

class Medium(ImageSpec):
    processors = [ResizeToFit(500)]
    format = 'JPEG'
    options = { 'quality' : 100 }

class Big(ImageSpec):
    processors = [ResizeToFit(1000)]
    format = 'JPEG'
    options = { 'quality' : 100 }

register.generator('models:thumbnail', Thumbnail)
register.generator('models:medium', Medium)
register.generator('models:big', Big)
