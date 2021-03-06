# django
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
# contrib
from contact_form.forms import AkismetContactForm
from contact_form.views import ContactFormView
# project
from django.conf import settings
from apps.views import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/',  include('django.conf.urls.i18n')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    # Registration urls
    url(r'^me-olvide-el-pass', auth_views.password_reset, name='password_reset'),
    url(r'^confirma-pass/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name="password_reset_confirm"),
    url(r'^pass-cambiado/$', auth_views.password_reset_complete, name="password_reset_complete"),
    url(r'^pass/ok/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'', include('registration.backends.default.urls')),
    # Contact form
    url(r'^contacta$', ContactFormView.as_view(form_class=AkismetContactForm), name='contact_form'),
    url(r'^contacta/', include('contact_form.urls')),
    # Front
    url(r'^$', views.FrontView.as_view(), name="front"),
    # Front
    url(r'^acerca$', TemplateView.as_view(template_name="pages/about.html"), name="about"),
    # Projects
    url(r'^proyectos$', views.ProjectsView.as_view(), name="projects"),
    # Project
    url(r'^proyectos/(?P<slug>.+)$', views.ProjectView.as_view(), name="project"),
)

if settings.DEBUG == True:
   urlpatterns += static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
   urlpatterns += static( settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT )
