from django.utils.translation import ugettext_lazy as _

""" Categories used by models """

PROJECT_CATEGORIES = (
    ('DI', _('Plataformas digitales')),
    ('HA', _('Prototipado de hardware')),
    ('IN', _('Instalaciones interactivas')),
    ('CU', _('Gestión y producción cultural')),
    ('DI', _('Diseño')),
    ('TA', _('Talleres y presentaciones')),
)

ENTITY_CATEGORIES = (
    ('CL', _('Cliente')),
    ('CO', _('Colaborador')),
    ('FI', _('Financiador')),
)
