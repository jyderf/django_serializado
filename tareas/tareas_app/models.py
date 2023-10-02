from django.db import models

# Create your models here.


class Proyecto(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=255)


class Tarea(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    estado = models.SmallIntegerField()
    idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idproyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
