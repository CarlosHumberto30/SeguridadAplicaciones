from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    numero = models.CharField(max_length=17,null=True,blank=True)
    status = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre



class version_estandar(models.Model):
    nombre = models.CharField(max_length=5000, null=False, blank=False)
    descripcion = models.CharField(max_length=5000, null=True, blank=True)
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Clientes, null=False, blank=False, on_delete=models.PROTECT)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=1)
    version = models.ForeignKey(version_estandar, null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Tema(models.Model):
    descripcion_tema = models.CharField(max_length=1000)
    descripcion = models.CharField(max_length=5000, null=True,blank=True)

    def __str__(self):
        return self.descripcion_tema



class colaborador_proyectos(models.Model):
    proyecto = models.ForeignKey(Proyecto,  null=False, blank=False, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

