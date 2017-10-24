# django
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
# contrib
from contact_form.forms import AkismetContactForm
from contact_form.views import ContactFormView
# project
from django.conf import settings
from apps.views import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/',  include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.FrontView.as_view(), name="front"),
    url(r'^',  include('apps.models.urls', namespace='modelforms')),
    # Registration urls
    url(r'', include('registration.backends.default.urls')),
    # Contact form
    url(r'^contacta$', ContactFormView.as_view(form_class=AkismetContactForm), name='contact_form'),
    url(r'^contacta/', include('contact_form.urls')),

)

if settings.DEBUG == True:
   urlpatterns += static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
   urlpatterns += static( settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT )
