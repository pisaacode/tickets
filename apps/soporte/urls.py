
from django.conf.urls import url
from django.views.generic import TemplateView
from apps.usuarios.views import user_login, logout_user

urlpatterns = [
    #url(r'^listado', TemplateView.as_view(template_name="base_angular.html"), name='listado_ticket'),
]