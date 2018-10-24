from django.conf.urls import url
from administracion.views import crearcliente,eliminarcliente,actualizarcliente,listarcliente,crearrol, \
                                listarrol, actualizarrol, eliminarrol, crearusuario, listarusuario, eliminarusuario,\
                                actualizarusuario, crearproyecto, listartema,creartema,listarproyecto, eliminarproyecto,\
                                actualizarproyecto, eliminartema, actualizartema,  \
    colaboradorproyecto,asignarcolaborador,validarnombreusuario,crearversion,listarversion, actualizarversion,eliminarversion


urlpatterns = [

    url(r'^crearcliente$', crearcliente, name='crearcliente'),
    url(r'^listarcliente$', listarcliente, name='listarcliente'),
    url(r'^editarcliente/(?P<pk>\d+)/$', actualizarcliente, name='editarcliente'),
    url(r'^eliminarcliente/(?P<pk>\d+)/$',eliminarcliente.as_view(), name='eliminarcliente'),


    url(r'^crearrol$', crearrol, name='crearrol'),
    url(r'^listarrol$', listarrol.as_view(), name='listarrol'),
    url(r'^editarrol/(?P<pk>\d+)/$', actualizarrol.as_view(), name='editarrol'),
    url(r'^eliminarrol/(?P<pk>\d+)/$', eliminarrol.as_view(), name='eliminarrol'),


    url(r'^crearusuario$', crearusuario, name='crearusuario'),
    url(r'^listarusuario$', listarusuario.as_view(), name='listarusuario'),
    url(r'^editarusuario/(?P<pk>\d+)/$', actualizarusuario, name='editarusuario'),
    url(r'^eliminarusuario/(?P<pk>\d+)/$', eliminarusuario.as_view(), name='eliminarusuario'),

    url(r'^crearproyecto$', crearproyecto, name='crearproyecto'),
    url(r'^listarproyecto$', listarproyecto, name='listarproyecto'),
    url(r'^editarproyecto/(?P<pk>\d+)/$', actualizarproyecto.as_view(), name='editarproyecto'),
    url(r'^eliminarproyecto/(?P<pk>\d+)/$', eliminarproyecto.as_view(), name='eliminarproyecto'),

    url(r'^creartema$', creartema.as_view(), name='creartema'),

    url(r'^listartema$', listartema.as_view(), name='listartema'),
    url(r'^editartema/(?P<pk>\d+)/$', actualizartema.as_view(), name='editartema'),
    url(r'^eliminartema/(?P<pk>\d+)/$', eliminartema.as_view(), name='eliminartema'),

    url(r'^crearversion$', crearversion.as_view(), name='crearversion'),

    url(r'^listarversion$', listarversion.as_view(), name='listarversion'),
    url(r'^editarversion/(?P<pk>\d+)/$', actualizarversion.as_view(), name='editarversion'),
    url(r'^eliminarversion/(?P<pk>\d+)/$', eliminarversion.as_view(), name='eliminarversion'),



     url(r'^proyectocolaborador/(?P<pk>\d+)/$', colaboradorproyecto.as_view(), name='proyectocolaborador'),
     url(r'^asignarcolaborador', asignarcolaborador, name='asignarcolaborador'),

     url(r'^validarnombreusuario', validarnombreusuario, name='validarnombreusuario'),

]