from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    idCategoria     = models.AutoField(primary_key=True,verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la Categoria")
    
    def __str__(self):
        return self.nombreCategoria
 
class Marca(models.Model):
    idMarca     = models.AutoField(primary_key=True, verbose_name="ID Marca")
    nombre      = models.CharField(max_length=100,verbose_name="Nombre de la marca")
    logo        = models.CharField(max_length=500, verbose_name="Logo de la marca")

    def __str__(self):
        return self.nombre

class Reparaciones(models.Model):
    idReparacion    = models.AutoField(primary_key=True, verbose_name="ID Reparacion")
    mecResponsable  = models.ForeignKey(User, on_delete=models.CASCADE)
    patente         = models.CharField(max_length=6, default="", verbose_name="Patente")
    marca           = models.ForeignKey(Marca,default="", null=False,  on_delete=models.CASCADE)
    modelo          = models.CharField(max_length=20,null=False,default="", verbose_name="Modelo")
    categoria       = models.ForeignKey(Categoria,default="", on_delete=models.CASCADE)
    log             = models.TextField(null = True, blank=True)
    Completa        = models.BooleanField(default=False)

    def __str__(self):
        return self.patente

    class Meta:
        ordering = ['Completa']