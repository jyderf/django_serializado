from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Tarea, Proyecto
from django.http.response import JsonResponse
from typing import Any
import json

# Create your views here.

class UsuarioView(View): #esta es la clase solo para usuario, aplica lo mismo para Tarea y Proyecto
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        if(id>0):
            usuarios=list(Usuario.objects.filter(id = id).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'message': "Succes", 'usuarios': usuarios }
            else:
                datos = {'message': "Usuario no encontrado ..." }
            return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'messaje':'Succes','usuarios':usuarios}
            else:
                datos = {'messaje': "Usuarios no encontrados..."}
        return JsonResponse(datos)
    
    def post(self,request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Usuario.objects.create(nombre=jd['nombre'] , correo_electronico = jd['correo_electronico'], contrasena =jd['contrasena'])
        datos = {'message':"Success"}

        return JsonResponse(datos)
    def put(self,request,id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id = id).values())
        if len(usuarios) > 0:
            usuario = Usuario.objects.get(id = id)
            usuario.nombre = jd['nombre']
            usuario.correo_electronico = jd['correo_electronico']
            usuario.contrasena = jd['contrasena']
            usuario.save()#para guardar los cambios
            datos = {'message': "Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Usuarios no encontrado... "}
    
    def delete(self,request, id):
        usuarios = list(Usuario.objects.filter(id = id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id = id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario no encontrado ..."}
        return JsonResponse(datos)
