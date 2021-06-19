from django.db import models


#Modelo para la categoria

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='id de categoria')
    nombreCategoria=models.CharField(max_length=50 ,verbose_name='Nombre de la categoria')

    def __str__(self):
        return (self.nombreCategoria)
    
class Producto(models.Model):
    idProducto=models.CharField(max_length=4,primary_key=True,verbose_name='Id del producto')
    marca=models.CharField(max_length=20,verbose_name='Nombre de el producto')
    modelo=models.CharField(max_length=20,verbose_name='Modelo del producto')
    nombre=models.CharField(max_length=20,verbose_name='Nomrbe del producto')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return(self.idProducto)


    #QUEDE EN EL MINUTO 01:12:35