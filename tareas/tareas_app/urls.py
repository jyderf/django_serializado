from django.urls import path, re_path
from .views import  UsuarioView #, TareaView, ProyectoView
urlpatterns = [
    path('listar_usuarios/', UsuarioView.as_view(), name='listar_usuarios'),
    path('listar_usuarios/<int:id>', UsuarioView.as_view(), name='listar_usuarios'),
   # path('listar_proyectos/', ProyectoView.as_view(), name='listar_proyectos'),
    #path('listar_proyectos/', TareaView.as_view(), name='listar_tareas'),
]
