from django.urls import path
from . import views

urlpatterns = [
    path('proyectos/', views.listarProyectos, name='listarProyectos'),
    path('proyectos/crear/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    #HABILIDADES

    path('habilidades/', views.lista_habilidades, name='lista_habilidades'),
    path('habilidades/crear/', views.crear_habilidad, name='crear_habilidad'),
    path('habilidades/editar/<int:pk>/', views.editar_habilidad, name='editar_habilidad'),
    path('habilidades/eliminar/<int:pk>/', views.eliminar_habilidad, name='eliminar_habilidad'),

]