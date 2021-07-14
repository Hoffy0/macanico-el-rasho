from django.db import models


# ############ Login/Register ################
# class User(models.Model):
#     idUser = models.IntegerField(primary_key=True, verbose_name="ID Usuario")
#     username = models.CharField(max_length=100, null=False)

#############################################

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True,verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la Categoria")
    def __str__(self):
        return self.nombreCategoria
 
class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name="Patente")
    marca = models.CharField(max_length=20, verbose_name="Marca Vehiculo")
    modelo = models.CharField(max_length=20,null=True,blank=True, verbose_name="Modelo")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.patente

class Slider(models.Model):
    idSlider = models.AutoField(primary_key=True,verbose_name="Id de Categoria")
    titulo = models.CharField(max_length=20, verbose_name="titulo slider")
    img = models.ImageField(upload_to= 'core/static/core/img/slider')
    def __str__(self):
        return self.titulo