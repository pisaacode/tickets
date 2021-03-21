from django.conf.urls import url
from apps.usuarios.views import user_login, logout_user

urlpatterns = [
    url(r'^login/$', user_login, name='login_user'),
    url(r'^logout/$', logout_user, name='logout_user'),
]