from django.conf.urls import url

#from apps.productos.views import AgregarView, productosView
from apps.matriculas.views import (
    MatriculaView,
    MatriculadoView,
    MatriculaInicioView,
    MatriculaLista
)

urlpatterns = [
    url(r'^$', MatriculaInicioView, name='inicio'),
    url(r'^matricular/$', MatriculaView.as_view(), name='matricular'),
    url(r'^listar/(?P<categoria>[1-9]{1,3})?/?$', MatriculaLista.as_view(), name='listar'),
    url(r'^ok/$', MatriculadoView.as_view(), name='ok')
]
