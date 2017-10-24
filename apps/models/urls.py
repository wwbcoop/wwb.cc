# django
from django.conf.urls import url
# project
from . import views

urlpatterns = [
    url(r'^crea/proyecto$',             views.ProjectCreate.as_view(), name="create_project"),
    url(r'^edita/proyecto/(?P<pk>.+)$', views.ProjectEdit.as_view(),   name="edit_project"),
    url(r'^borra/proyecto/(?P<pk>.+)$', views.ProjectDelete.as_view(), name="delete_project"),
]
