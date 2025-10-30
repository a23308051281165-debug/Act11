from django.urls import path
from . import views

app_name = 'app_productos'

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
]
