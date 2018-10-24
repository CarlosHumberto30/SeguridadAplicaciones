from django.conf.urls import url
from main.views import *



urlpatterns = [
    url(r'^$', home, name='home'),
    #url(r'^login/$', views.login_page, name='login'),
    url(r'^login/$', Login.as_view() , name='login'),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^setproyect/(?P<next>.*)/$', seleccionar_proy, name="setproyect"),
    url(r'^password/$', change_password, name='change_password'),
    url(r'^locked/$', locked_out, name='locked_out'),
]
