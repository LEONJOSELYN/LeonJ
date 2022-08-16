from django.urls import path
from . import views
urlpatterns = [
path('', views.holamundoCore, name='core'),
path('INICIO', views.INICIO, name='inicio1'),
path('Contactos', views.Contactos, name='contacto1'),
path('Nuestrosproductos', views.Nuestrosproductos, name='nuestros1'),
path('Quienessomos', views.Quienessomos, name='quienes1'),
path('Bebidas', views.Bebidas, name='bebidas1'),
path('Dulces',views.Dulces, name='dulces1'),
path('Verduras',views.Verduras, name="verduras1"),
path('Carnes',views.Carnes, name='carnes1'),
path('Higiene',views.Higiene, name='higiene1'),
path('Quejas',views.Quejas, name='quejas1'),
path('Trabaja',views.Trabaja, name='trabaja1'),
path('inicioh',views.inicioh, name='inicioh')
]